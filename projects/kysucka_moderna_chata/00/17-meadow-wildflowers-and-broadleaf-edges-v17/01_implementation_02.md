# V17 implementation — meadow wildflowers, broadleaf forest-edge groups, and living front-loop trail edges

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17
Worker session ordinal: 01
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker (same-session continuation of Planner 01/01–01/02)
Phase: implementation
Task identity: NATURE-DETAIL-V17-IMPL — normalize Stage-0 assets, validate Stage-1 pilot, and build/validate/render Stage-2 full candidate V17 from V16 B
Delivery route: manual Cooperator delivery
Continuity anchor: accepted V17 implementation plan `01_report_01.md` (exchange 01/02) together with asset/cohort report `01_report_00.md` (SHA-256 `d66746fc408fc21ad52a69815ef0c894202c18bf422dbca8b41ab5757e92dd02`, exchange 01/01), reconciled and accepted by this whole's ORCHESTRATOR on 2026-11-19 (recorded in `00_notes.md`)
Authority renewal: prior planning authority expired at `01_report_01.md`; this prompt grants complete new bounded implementation authority with `Native planning mode: not-used`. Retained context is convenience, not authority. Re-gate repository, input hashes, and process state yourself; stop on any conflict between retained context and current evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: multi-stage asset normalization with KTX2 sidecar packing and offline cold-reopen proof, pilot-to-full expansion across botanical/broadleaf/trail-lip layers, exhaustive basal-support and crown/corridor clearance verification, and serialized high-resolution foreground border and low-witness CPU4 renders inside strict memory/process guards
Recommended context capacity: approximately 250k tokens

## Binding specification and goal

Your accepted plan `01_report_01.md` (§§1–6, supported by `01_report_00.md`) is the binding technical specification for **V17**. Implement it inside `work/v17/nature_detail_01/` starting from immutable **V16 B** (`work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`, SHA-256 `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`):

1. **Stage 0 — Normalize and pack offline assets (`work/v17/nature_detail_01/assets/`):**
   - Verify the pinned SHA-256 hashes of the raw CC0 assets (`Wildflower Patch v1 LOD0` `8fd2262da4a62e4d16c97f4bfd24c0aff1498f08fa34c3245cee13a40aefc096`, `European Beech v1 LOD1` `20be1b2801f72cebeb3d5b91a5b275e7645de54d160771e881ea9061b8e726c3`, `European Beech v1 LOD2` `f52e44fc1de7bcd31c1eb6a2cdcd509e5fae18d7ab2162f89d1bdbe17eac5f00`, `Silver Birch v1 LOD1` `ba9ccd03ba2d0ad21f82eb6fd9934712822946b6c869069a17f3d5580b7ddedc`, `Silver Birch v1 LOD2` `a6ae6b4384feeb955fdd5e23d21fa5d1feb821ddda1dd1d95892b82a1728bb92`, and `Poly Haven Dandelion 01 1K Blend` `9751bb96fe8a10f19cd04c736e1417825f71aa7fbf1cb632e8c5ebc08f77a3d4` + its 5 texture maps).
   - Externalize each tevy KTX2 bufferView to a local `.ktx2` sidecar in the disposable runtime directory, import via stock Blender 5.3.0 `.gltf` (`import_ktx_texture=True, import_pack_images=True, merge_vertices=False`), append the two `Dandelion 01` LOD2 objects (`dandelion_01_a_LOD2`, `dandelion_01_b_LOD2`), build and pack `assets/v17_masters.blend`, cold-reopen it in a separate isolated Blender process to verify packed image dimensions, alpha ranges, finite non-constant pixels, and material roles, and write `assets/ASSET_MANIFEST.md` (author, URL, license, version, raw and normalized SHA-256, and exact modifications while preserving existing project asset credits).
2. **Stage 1 — Pilot (`stage="pilot"`):**
   - Apply `apply_v17(scene, config, project_root, stage="pilot")` from fresh V16 B covering the pilot footprint (§2: 4 forced botanical anchors + seeded clusters in the buffered pilot hull, Zone B and both trail shoulders at `21 ≤ s ≤ 36 m`, and broadleaf group `R` `R1, R2, R3` with its Zone C understorey), create fixed low witness camera `CAM_V17_LOW_DETAIL`, and save `checkpoints/pilot_v17.blend`.
   - Render `renders/pilot_valley_960.png` (`CAM_V11_VALLEY_REVIEW`, `960 × 540`) and `renders/pilot_low.png` (`CAM_V17_LOW_DETAIL`, `3200 × 1800`) and verify the pilot gates (§6.2: resolved white/yellow flower anchors and curved seed stems in `pilot_low.png`, continuous gravel core + irregular fine edge + supported leaves/blades at `s = 30 m`, retained V16 B slope palette and readable `R3` crown in `pilot_valley_960.png`) before expanding to Stage 2.
3. **Stage 2 — Full V17 candidate (`stage="full"`) and matched comparison renders:**
   - Apply `apply_v17(scene, config, project_root, stage="full")` from fresh V16 B across full Zones A, B (`7.5 ≤ s ≤ 42 m`), C (`R, L, D`), full front-loop trail edges (`5 ≤ s ≤ 44 m`), and all 8 broadleaf placements (`R1, R2, R3, L1, L2, D1, D2, O1` replacing the 4 specified edge conifers `V11_TREE_01610, 02456, 01307, 03274` → `6,196` surviving V11 points). Save `checkpoints/candidate_exterior_v17.blend` with `CAM_V11_VALLEY_REVIEW` and the established `960 × 540` CPU4 / 96-sample / OIDN Accurate/High comparison profile active.
   - Verify second-application idempotence, fresh-input replay from pristine V16 B (without saving), and offline cold reopen of `candidate_exterior_v17.blend` by exact semantic hash equality, plus all 6 existing `IsViewport` working branches and the 3 new V17 `IsViewport` working branches (`V17_BOTANICAL_IsViewport`, `V17_BROADLEAF_IsViewport`, and the V17 trail-edge `IsViewport` arm), exhaustive basal support, crown/sightline clearances, and trail core protection (`|lateral| ≤ 0.480 m`).
   - Render the matched comparison pairs one-by-one on CachyOS (measuring wall time and peak RSS for every render):
     - `CAM_V11_VALLEY_REVIEW` full frame `960 × 540`: `renders/V17_valley_960.png` paired with immutable V16 B `work/v16/meadow_trail_01/renders/B_v16_960.png` (after confirming identical render profile).
     - `CAM_V11_VALLEY_REVIEW` 1:1 foreground border from `5760 × 3240` top-left pixel rectangle `[504, 2000, 5184, 3240)`: `renders/B_foreground.png` (from V16 B) and `renders/V17_foreground.png` (from V17).
     - Fixed low witness `CAM_V17_LOW_DETAIL` at `3200 × 1800`: `renders/B_low.png` (from V16 B with `CAM_V17_LOW_DETAIL` added in memory without saving V16 B) and `renders/V17_low.png` (from V17).
   - If a concrete reproducible visual defect appears in the Stage-2 renders, you may execute at most **one** targeted correction (archiving pre-correction outputs under `before_c01/` per the plan allowlist and re-verifying all final gates and affected render pairs).

## Repository gate and exactbaseline

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17`

Project repository gate:
- Standalone checkout at `R`, branch `main`, expected HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5` (tracked working tree and index clean; untracked owner file `reference/01.png` with SHA-256 `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` is classified under RF-12 as `unrelated-owner-work` and must remain untouched).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap` (gitlink = submodule HEAD).
- Meta repository: `/home/agile/meta`, branch `main`, HEAD `abfb0ea0226dab1db554abcd47b4cc0a3fc289c1`.

Immutable input hashes (verify before and after execution):
- `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`: `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `work/v16/meadow_trail_01/source/meadow_trail_v16.py`: `16bde4cf14182b99ae4467cdf4f052ab9067c7a2b46613648140775a4f09266e`
- `work/v16/meadow_trail_01/source/meadow_trail_v16.json`: `1298218692c8fe88f27008df9eab287b2f5c3e7bb62866f762df883e748243fb`
- `work/v16/meadow_trail_01/renders/B_v16_960.png`: `92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6`
- `work/v16/meadow_trail_01/renders/C_v16_c01_960.png`: `62f4f5afc34f246f125c4da7d22bdb331fde96ac7713b59e6d31420aa196b317`
- `reference/01.png` (= `/home/agile/Projects/chata/chatgpt/01.png`): `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`

Mandatory reading: governing WORKER spine (`.ap/AP.md` Semantic Authority + WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18); `.ap/AP_WORKER.md` Worker Session Target + Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Implementation Authority Record, Mutation Axes, Delivery Record; project `AGENTS.md`; `T/00_handout.md`; `T/00_notes.md`; `T/01_report_00.md`; and your accepted plan `T/01_report_01.md`.

## Execution route and resource/process guards

Canonical execution route: **isolated native Blender 5.3.0 CLI route** (`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`), explicitly activated for this isolated exterior task because Michal owns the live Blender GUI (`PID 2452`, `start_ticks 12233`) and live MCP is prohibited.

- Run at most **one** owned background Blender child at a time, serialized sequentially.
- Launch with `nice -n 10`, `PYTHONPYCACHEPREFIX` inside the job's `runtime/` directory, `PYTHONDONTWRITEBYTECODE=1`, `sys.dont_write_bytecode = True`, and process-local `BLENDER_USER_CONFIG`, `TMPDIR`, `TMP`, `TEMP` under `R/work/v17/nature_detail_01/runtime/<job>/` using a copy of `work/v12/profile_03/isolated_config/userpref.blend`. (Any standard Python `__pycache__/*.pyc` files under `/home/agile/Applications/Blender/` or project `scripts/__pycache__` remain explicitly permitted as benign interpreter cache.)
- Before every child launch, verify: no foreign background Blender exists, owner GUI `PID 2452` (`start_ticks 12233`) is untouched, and system available RAM is **≥12 GiB**.
- Sample resources every ~1 s during execution: stop only your own child if own RSS exceeds **8 GiB** (early-stop guard at **7.5 GiB**), or if system available RAM falls below **6 GiB** on two consecutive samples; use a **240 s** watchdog for `960 × 540` jobs and a **900 s** watchdog for `3200 × 1800` / `5760 × 3240` border jobs.
- Verify before and after every child that global `/home/agile/.config/blender/5.3/config/userpref.blend` (`8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`) and owner GUI `PID 2452` (`start_ticks 12233`) are unchanged.

## Authority and mutation axes

Exact changed-path allowlist (all project writes must reside under `R/work/v17/nature_detail_01/`):
- `work/v17/nature_detail_01/source/nature_detail_v17.{py,json}`
- `work/v17/nature_detail_01/assets/ASSET_MANIFEST.md`
- `work/v17/nature_detail_01/assets/v17_masters.blend`
- `work/v17/nature_detail_01/assets/raw/{wildflower-patch-v1-lod0,european-beech-v1-lod1,european-beech-v1-lod2,silver-birch-v1-lod1,silver-birch-v1-lod2}.glb`
- `work/v17/nature_detail_01/assets/raw/dandelion/dandelion_01_1k.blend`
- `work/v17/nature_detail_01/assets/raw/dandelion/textures/dandelion_01_{alpha_1k.png,nor_gl_1k.exr,diff_1k.jpg,mask_1k.png,rough_1k.exr}`
- `work/v17/nature_detail_01/checkpoints/{pilot_v17,candidate_exterior_v17}.blend`
- `work/v17/nature_detail_01/renders/{pilot_valley_960,pilot_low,B_foreground,V17_foreground,B_low,V17_low,V17_valley_960}.png`
- `work/v17/nature_detail_01/proofs/{assets,preflight,pilot,full,idempotence,replay,cold,support,clearance,render_metrics,visual_review}.json`
- `work/v17/nature_detail_01/proofs/artifacts.sha256`
- `work/v17/nature_detail_01/proofs/{assets,pilot,full,replay,cold,pilot_valley_960,pilot_low,B_foreground,V17_foreground,B_low,V17_low,V17_valley_960}.log`
- `work/v17/nature_detail_01/runtime/{assets,pilot,full,replay,cold,pilot_valley_960,pilot_low,B_foreground,V17_foreground,B_low,V17_low,V17_valley_960}/**`
- `work/v17/nature_detail_01/before_c01/checkpoints/{pilot_v17,candidate_exterior_v17}.blend` (only if the single optional correction is triggered)
- `work/v17/nature_detail_01/before_c01/renders/{pilot_valley_960,pilot_low,V17_foreground,V17_low,V17_valley_960}.png` (only if the single optional correction is triggered)
- `work/v17/nature_detail_01/before_c01/proofs/{config,render_metrics,visual_review}.json` (only if the single optional correction is triggered)
- Direct-write terminal report `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_02.md` (if your client permits the write; otherwise return the complete report in session output for Orchestrator persistence).

Network authority: bounded HTTPS fetches permitted **only** in Stage 0 for the exact pinned SHA-256 asset files listed in your plan §6.1 (`tevy` v1 GLBs and `Poly Haven Dandelion 01` 1K Blend + 5 maps) if not already cached locally; every downloaded file must match its pinned SHA-256 before use, and Stage 1 / Stage 2 / replay / cold reopen must run 100% offline.

Negative authority:
- No writes to any tracked project file (`model/`, `scripts/`, root `assets/`, `docs/`, `AGENTS.md`, `README*`), `reference/01.png`, or any prior `work/v05`–`work/v16` file.
- No live MCP calls (`tools.blender.*` prohibited), no GUI window launch, no touching or signalling Michal's GUI `PID 2452`, no Blender importer modification, no package/runtime installation, no Git writes in any repository, no 2D image retouch/compositing, and never emit the literal project closure signal.

Repository mutation: only new `R/work/v17/nature_detail_01/**` paths in the exact allowlist above
Host/remote mutation: only owned isolated headless Blender child processes using `R/work/v17/nature_detail_01/runtime/**` and bounded Stage-0 asset fetches matching pinned SHA-256 hashes; zero persistent host mutation
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_02.md`

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
Downloadable prompt filename: 01_implementation_02.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17
Report filename: 01_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Validation and required evidence

Evidence tier: E2
Evidence tier basis: reversible isolated candidate build, offline asset normalization, pilot verification, and matched native CPU4 renders under `work/v17/nature_detail_01/`
Combined implementation envelope: allowed
Authorized implementation stages: (0) preflight & Stage-0 asset normalization + cold-reopen texture proof; (1) Stage-1 pilot build & matched pilot renders (`pilot_valley_960.png`, `pilot_low.png`) + geometry/mask/pixel verification; (2) Stage-2 full candidate build (`candidate_exterior_v17.blend`), second-apply idempotence, fresh-input replay, offline cold reopen, working-branch/support/clearance proofs, and serialized matched comparison renders (`V17_valley_960.png`, `B_foreground.png`, `V17_foreground.png`, `B_low.png`, `V17_low.png`), plus at most one bounded correction if a concrete visual defect is observed; (3) visual review metrics, `proofs/artifacts.sha256`, and terminal report `01_report_02.md`
Implementation stage gates: every failed gate stops the sequence; Stage 1 must pass before Stage 2 begins
Independent acceptance: not-required
Rollback or recovery checkpoint: immutable V16 B (`5d82ecf4...`) and all prior `work/` directories remain untouched; all V17 outputs stay isolated in `work/v17/nature_detail_01/`
Terminal implementation report point: one, after Stage 3

Stopping conditions: failed repository/input/asset SHA-256 gate; foreign background Blender contention; own RSS >8 GiB or system available RAM <6 GiB; support/clearance/idempotence/replay/cold-reopen failure that cannot be resolved inside the single correction budget.

Completion and report contract: begin `01_report_02.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-meadow-wildflowers-and-broadleaf-edges-v17`, `01`, `03`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: implementation-PASS | not-applicable`, `Start commit` / `End commit`, changed files and SHA-256 table including `candidate_exterior_v17.blend`, `nature_detail_v17.py`, `v17_masters.blend`, and all rendered PNGs, validation summary with render wall times, peak RSS, minimum available RAM, support/clearance/working-branch/replay/cold results, and 10–90% trail-edge transition widths at `s = 16, 24, 30, 36, 42`, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-mutation`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Write `T/01_report_02.md` and read it back completely (or return the complete report text in session output if direct write is blocked).

Authority expiry: this terminal report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.
