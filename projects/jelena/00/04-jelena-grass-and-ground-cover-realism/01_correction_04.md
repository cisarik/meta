# Bounded Visual Correction — Jelena grass and ground-cover realism (`v006`)

Persistent role identity: WORKER
Logical whole identity: jelena-grass-and-ground-cover-realism
Worker session ordinal: 01
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker
Phase: Implementation
Task identity: JELENA-GRASS-AND-GROUND-COVER-REALISM-CORRECTION-01
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — targeted parameter and geometry refinement inside the existing `scripts/grass_ground_cover_v006.py` architecture.
Independence required: no
Implementation authority: explicit
Exact baseline: cisarik/jelena HEAD c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e on main, with current candidate Jelena/Jelena_Realistic_v006.blend (SHA-256 7aa4403f99c5e69a9b38537d3157db06d533ac77c1e9b4d109362c6ab7ba8267) and preserved checkpoint .local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend (SHA-256 892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4)
Changed-path allowlist: Jelena/Jelena_Realistic_v006.blend, scripts/grass_ground_cover_v006.py, evidence/grass-006/camera-a-after.png, evidence/grass-006/overview-after.png, evidence/grass-006/grass-detail-after.png, evidence/grass-006/access-clearance.png, evidence/grass-006/manifest.json, README.md
Implementation boundaries: refine v006 clump footprint spread, clump instance density, noise patchiness, and grass shader brightness in Jelena_Realistic_v006.blend and scripts/grass_ground_cover_v006.py; preserve before renders, working v005, checkpoints, and all non-grass datablocks byte-for-byte; no Git commit or push in this exchange
Continuity anchor: implementation report `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_03.md` (SHA-256 `8c34812c0577f3e8be24662fd7f9915cb142c54e07b37426582fc001d2938080`) from Worker session `01` / exchange `04`.
Authority renewal: prior authority expired at the submission of `01_report_03.md`; this prompt grants one bounded visual correction in the same healthy Worker session before Cooperator visual acceptance. Retained context is convenience only, not authority; re-gate repository and live Blender state before mutating and stop on any conflict with current repository or scene evidence.
Evidence posture: non-independent

## 1. Orchestrator Visual Inspection Findings (Why Correction 01 is Issued)

Technical execution, clearance assertions (`0` violations), Scene-B preservation (`22878d79...`), idempotence, and memory performance (`<= 1.09 GiB` sampled RSS for `v006` renders, `17–29 s` per still) all passed in `01_report_03.md`. However, direct Orchestrator visual inspection of `camera-a-after.png`, `overview-after.png`, `grass-detail-after.png`, and `access-clearance.png` identified two concrete in-scope visual defects that prevent the candidate from meeting the acceptance gate (*"Grass visibly becomes denser and more natural in Camera A and overview, with clear tapered/curved form in the detail"*):

1. **Defect A — Sparse clump-center density (`127,418` clumps = `1.04×` of the `122,899` baseline) combined with tight root disks (`25–45 mm`) creates isolated polka-dot tufts on bare ground**:
   - At `38.45` clumps/m², clump centers are `~161 mm` apart on average while each clump's root disk is only `50–90 mm` wide. Consequently, `~70–80%` of the clearing in `camera-a-after.png`, `overview-after.png`, `grass-detail-after.png`, and `access-clearance.png` is exposed flat `Lesná pôda` mesh surrounding isolated small tufts.
2. **Defect B — `Tráva • pokryv • A` mid-blade colour is darker than the sunlit `Lesná pôda` ground**:
   - Because the mid-blade linear RGB `(0.055, 0.120, 0.018)` is darker than the sunlit olive-brown soil, distant tufts in `camera-a-after.png` and `overview-after.png` read as dark spots/speckles against a lighter floor rather than sunlit meadow grass.

## 2. Exact Bounded Correction Specification

Update `/Users/agile/Projects/jelena/scripts/grass_ground_cover_v006.py`, rebuild the owned grass datablocks in `Jelena/Jelena_Realistic_v006.blend`, re-run the idempotence/clearance/preservation checks, and re-render the four `after` images (`camera-a-after.png`, `overview-after.png`, `grass-detail-after.png`, `access-clearance.png`; keep the three `*-before.png` files unchanged):

1. **Higher Clump Density (`~3.8×–4.5×` clump count) with 24 Blades per Clump (`~15×–20×` effective blade density)**:
   - Build each of the 9 prototypes (`Tráva v006 • 00 krátka A` .. `08 vyššia C`) with **24 curved, tapered, V-folded blades per clump** (all using `3` longitudinal segments = `10` triangles/blade = `240` triangles/clump = `2,160` unique triangles total across all 9 prototypes) so each clump is half the triangle weight while clump count increases ~3.8×–4.5×.
   - Calibrate the global distribution density so the evaluated `v006` scatter produces **`460,000` to `540,000` clumps on common support** (`~142–167` clumps/m², average spacing `~77–84 mm`), yielding **`11.0M` to `13.0M` rendered blades on common support** (`~18.5×–21.8×` the `597,175`-blade `1×` reference census, and **both ~4× more clumps AND ~1.4×–1.5× more blades than even the 14× working state**, while keeping transformed instanced triangles around `~110M–130M`, well within our `4.2 GiB` RSS budget since `74.4M` triangles used only `1.09 GiB`!).
   - If sampled RSS during evaluation or rendering exceeds `4.2 GiB`, step down the calibrated target to `360,000–420,000` clumps (`~8.6M–10.1M` blades, `~14.5×–16.9×` the `1×` blade census) so memory stays safely below `4.2 GiB`. Record both the achieved clump-count ratio and achieved blade-count ratio in `manifest.json` and the report.
2. **Wider Clump Root Disks, Outward Splay, and Fuller Blade Silhouette**:
   - Give blades an outward-biased bend direction (`normalize(0.70 * radial_outward + 0.30 * random_unit_xy)` when `|root_xy| > 1e-4`, else random XY) so clumps splay outward and interlace with neighboring clumps instead of forming vertical cylinders:
     - **Short (`00..02`, `35%` share outside edge zone)**: unscaled blade height `0.065–0.100 m`, root width `0.0048–0.0075 m`, root disk radius **`0.055 m`**, outward bend **`0.025–0.050 m`**, segments `3`, max prototype XY radius bound `R <= 0.110 m`.
     - **Main (`03..05`, `50%` share outside edge zone)**: unscaled blade height `0.115–0.175 m`, root width `0.0055–0.0088 m`, root disk radius **`0.075 m`**, outward bend **`0.040–0.075 m`**, segments `3`, max prototype XY radius bound `R <= 0.155 m`.
     - **Accent (`06..08`, `15%` share outside edge zone)**: unscaled blade height `0.185–0.255 m`, root width `0.0060–0.0098 m`, root width taper `(1 - t)^1.15`, root disk radius **`0.085 m`**, outward bend **`0.055–0.095 m`**, segments `3`, max prototype XY radius bound `R <= 0.185 m`.
   - Instance Z scale `0.90..1.12`; base XY scale `0.90..1.15` (tapered near access edges as below).
3. **Turf-First Patchiness (`80–85%` Continuous Overlapping Meadow, `15–20%` Irregular Soil Pockets)**:
   - Adjust the point-domain world-space Noise modulation (`scale 0.45`, `detail 2.5`) so `~80–85%` of the clearing retains high, overlapping clump coverage while `~15–20%` forms organic lower-density pockets where `Lesná pôda` remains readable between tufts (e.g., map Noise `Fac` via Map Range `From Min 0.28`, `From Max 0.56` -> `To Min 0.18`, `To Max 1.0`, clamped).
4. **Brighter, Sunlit Meadow Shader (`Tráva • pokryv • A`)**:
   - Update the longitudinal UV (`t`) colour ramp in `Tráva • pokryv • A` so sunlit mid-blades and tips read warmer and brighter than the shaded roots and soil:
     - `t = 0.00` (root): linear RGB `(0.022, 0.045, 0.010)`
     - `t = 0.25` (lower blade): linear RGB `(0.058, 0.138, 0.022)`
     - `t = 0.62` (mid blade): linear RGB `(0.115, 0.245, 0.038)`
     - `t = 1.00` (sunlit tip): linear RGB `(0.245, 0.370, 0.070)`
   - Keep `Object Info -> Random` hue variation `±0.03` and value factor `0.85..1.15`, Principled roughness `0.68`, IOR `1.45`, Specular IOR Level `0.28`, and `16%` Translucent BSDF mix.
5. **Post-Distribution Clearance with Measured Prototype Radii**:
   - Use each family's actual measured maximum XY radius `R` (or conservative bound covering the wider clumps) in the post-distribution edge filter:
     - Within `0.25 m` of the projected `Maska trávy v006 • A` boundary, force short variants (`0..2`), set `effective_xy_scale = min(s, (d - 0.008) / R_short)`, and delete roots inside the mask or where `effective_xy_scale < 0.35`.
     - Outside `0.25 m`, ensure `effective_xy_scale = min(s, (d - 0.008) / R_family)` so no main or accent clump placed just beyond `0.25 m` can ever reach across the `8 mm` safety margin!
     - Re-run the full-census clearance assertion (`0` roots inside mask, `0` violations of `R * effective_xy_scale + 0.008 <= d` across all final instances).

## 3. Authority, Mutation Axes, and Trace Delivery

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism
Trace project key: jelena
Trace logical-whole projection identity: jelena-grass-and-ground-cover-realism
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_correction_04.md
Destination path: /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism
Report filename: 01_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: Jelena/Jelena_Realistic_v006.blend, scripts/grass_ground_cover_v006.py, evidence/grass-006/camera-a-after.png, evidence/grass-006/overview-after.png, evidence/grass-006/grass-detail-after.png, evidence/grass-006/access-clearance.png, evidence/grass-006/manifest.json, README.md
Host/remote mutation: live Blender 5.2.3 LTS session on 127.0.0.1:9876 — rebuild owned v006 grass datablocks in Jelena/Jelena_Realistic_v006.blend, sequential single-still Cycles CPU renders of the four after/clearance PNGs, and save Jelena/Jelena_Realistic_v006.blend
Trace persistence: direct-write /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_04.md
```

```text
Evidence tier: E2
Evidence tier basis: bounded visual correction of v006 grass density, clump spread, and shader brightness with full clearance/preservation/idempotence assertions
Authorized implementation stages: (1) pre-mutation re-gate on clean v006 and preserved baseline/checkpoint hashes; (2) update scripts/grass_ground_cover_v006.py and run patch preview + full idempotent build; (3) sequential renders of camera-a-after.png, overview-after.png, grass-detail-after.png, and access-clearance.png with sampled ps RSS monitoring; (4) visual inspection, full clearance/preservation/idempotence assertions, render-settings restoration, save v006, update manifest.json, and write 01_report_04.md
Combined implementation envelope: allowed
Implementation stage gates: stop if sampled RSS breaches 5.0 GiB, if any clearance/preservation assertion fails, or if any pre-v006 .blend or *-before.png hash changes
Rollback or recovery checkpoint: /Users/agile/Projects/jelena/.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend (SHA-256 892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4)
Activated stricter profile: none
Terminal implementation report point: after Jelena_Realistic_v006.blend, scripts/grass_ground_cover_v006.py, the four updated after/clearance PNGs, and manifest.json are saved and verified on disk, and 01_report_04.md is written and read back
```

## 4. Validation and Report Contract

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: scripts/grass_ground_cover_v006.py validation suite
Affected tests: scripts/grass_ground_cover_v006.py read-only validation and assertion suite
New causal regression: assert 460k-540k common-support clumps (or 360k-420k if 4.2 GiB soft gate triggers), 24 blades/clump, all 9 variants active, 0 roots inside mask, 0 violations of R * effective_xy_scale + 0.008 <= d, idempotence across two consecutive full builds, and unchanged preservation digest 22878d79fdd35b460714cab3d5b7b47e3bd3327dddff018f70b026468a660987
Broad or full suite: not-used
Runtime or testbed: live Blender 5.2.3 LTS via local blender MCP
Independent acceptance: not-required
```

Completion and report contract:

- Begin `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_04.md` with `### Report for ORCHESTRATOR_CHAT` and echo the three coordinate fields from this prompt once.
- Report `status: PASS`, `Phase-qualified result: implementation-PASS`, `Start commit` and `End commit` = `c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e`, `Report justification: new-mutation`, and `Logical-whole closure: not-closed`.
- Include: updated SHA-256 hashes, quantitative density table (showing both clump-count ratio and blade-count ratio against the `122,899` / `614,495` 1× reference and `1,720,525` / `8,602,625` 14× spike state), clearance verification, per-render seconds and sampled `ps` RSS in KiB, direct visual comparison of the new `after` images against the previous dotted pass, `Orchestration critique`, `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`, and `Authority expiry`.
- Authority expires upon submission of this terminal report.
