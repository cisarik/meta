# V16 bounded visual correction c01 — stronger golden slope/meadow contrast and visibly irregular vegetated trail edges

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16
Worker session ordinal: 01
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker (same-session continuation after 01/02)
Phase: implementation
Task identity: MEADOW-LIGHT-TRAIL-V16-C01 — execute the single reserved c01 visual correction for golden slope/meadow contrast and soft irregular trail edges
Delivery route: manual Cooperator delivery
Continuity anchor: terminal implementation report `01_report_01.md` (SHA-256 `07e55c077a9306b9f972af6f78770ea3fcc2c40aa6e689acba5bd057df8f8a00`) for MEADOW-LIGHT-TRAIL-V16-IMPL, exchange 01/02, reconciled by this whole's ORCHESTRATOR on 2026-11-19 (record in `00_notes.md`)
Authority renewal: prior implementation authority expired at `01_report_01.md`; this prompt grants the single reserved bounded correction (`c01`) planned in `01_report_00.md` §5. Retained context is convenience, not authority. Re-gate repository, immutable inputs, frozen 01/02 outputs, and process state yourself.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: calibrating shader contrast and trail-edge encroachment to satisfy all 13 crop/transect thresholds while preserving the verified forest-shadow/cottage/sky balance, exhaustive basal support, and isolated CPU4 resource bounds
Recommended context capacity: approximately 250k tokens

## Acceptance/correction status and root-cause analysis

Orchestrator directly inspected `work/v16/meadow_trail_01/renders/B_v16_960.png`
(`92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6`) and
reconciled `01_report_01.md`:

1. **What succeeded and MUST be preserved unchanged in `c01`:**
   - All technical gates (staged preservation, second-apply idempotence,
     fresh-input replay, cold reopen, 87-image portability, all six
     `_working_branch` checks, and exhaustive basal-vertex/hull support).
   - `V16_WORLD_MEADOW_BALANCE` (`fill_strength = 0.92`,
     `fill_tint = [1.0, 0.94, 0.80, 1.0]`): shaded left forest median luma
     reached **`29.095`** (target `28–33`, p5 `18.637 ≥ 18`), cottage
     shadow/lit median ratio is **`0.6481`** (target `0.60–0.71`), and sky RGB
     matches V15 C within `0.002` encoded levels with zero new clipping. Keep
     this world and key lighting exact.
2. **Causal diagnosis of the six unmet visual/crop criteria in `B_v16_960.png`:**
   - **Cause A (smooth olive slopes, zero left-slope golden fraction, low front/slope luma std and high-pass RMS):**
     In `meadow_trail_v16.py` lines 74–94:
     (i) `D = smoothstep(0.18, 0.62, dot(N, sun))` evaluates near `0` on the
     left slope because the key sun (`azimuth 285°`) grazes or faces the right
     slope, leaving the left slope with `0%` golden pixels (`5.303` std vs
     `≥5.5`).
     (ii) Blender's 3D `ShaderNodeTexNoise` `Fac` clusters tightly around `0.5`,
     so `F = smoothstep(0.36, 0.68, 0.65*N18 + 0.35*N3)` has weak contrast, and
     the golden colors (`terrain_gold [0.30, 0.255, 0.065]`,
     `meadow_gold [0.38, 0.32, 0.075]`) have nearly the same luminance as the
     base olive green. Consequently, mixing toward gold barely changed luma
     standard deviation (`Front meadow 9.816` vs `≥10.2`, `Right slope 7.356`
     vs `≥7.8`, `Front high-pass RMS 6.259` vs `≥6.3`).
   - **Cause B (trail still reads as a sharp uniform ribbon; foreground edge-width ratio `0.9948` vs `≥1.25`):**
     In `meadow_trail_v16.py` lines 147 and 167–190:
     (i) `Eσ(s) = h(s) - a(s)*(0.02 + 0.04*noise1)` shifts the effective edge
     inward by only **2–6 cm**, and in `V16_TRAIL_SHOULDER_FIELDS` the
     transition from loam to grass (`From Min = 0.12 m`) starts **outside** the
     `V07_TRAIL_MESH` ribbon (`abs(lateral) ≤ h(s)`). As a result, the entire
     physical top of `V07_TRAIL_MESH` up to its 15 mm lip remains bright
     gravel/loam with a razor-sharp geometric edge at `abs(lateral) = h(s)`.
     (ii) Shoulder tufts were tiny (`0.06–0.14 m` height, `0.075 m` radius) and
     kept outside both `V07_TRAIL_MESH` (`if gravel.hits(box): reject`) and
     `d < 0.022 m`, so they never visually broke up or overlapped the ribbon
     border at `960 × 540`.

## Exact c01 technical adjustments to implement

Create `work/v16/meadow_trail_01/source/meadow_trail_v16_c01.py` (exposing
`apply_v16_c01(scene, config, ROOT)`) and
`work/v16/meadow_trail_01/source/meadow_trail_v16_c01.json`, starting from the
same immutable V15 C input
(`work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend`), while
keeping all 01/02 files frozen:

1. **Stronger golden sunlit patches & macro/micro luma contrast on slopes and meadow:**
   - Widen the sun/sky-facing factor so both right and left undulating slopes
     receive warm golden highlights on their upper/sun-ward facets while
     retaining directional grounding: use
     `D_raw = smoothstep(-0.12, 0.50, dot(normalized_unbumped_normal, key_source_vector))`
     plus an upward-normal sky-grazing term
     `D = clamp(0.26 * smoothstep(0.55, 0.98, Normal.z) + 0.74 * D_raw, 0.0, 1.0)`.
   - Sharpen the warm-patch field `F` across the centered noise range:
     `F = smoothstep(0.43, 0.57, 0.58*N18 + 0.42*N3)` and add a complementary
     cool-trough factor `T = smoothstep(0.56, 0.42, 0.58*N18 + 0.42*N3)`.
   - Use brighter, warmer golden-green target palettes (`terrain_gold` linear
     RGB **`[0.48, 0.37, 0.065]`**, `meadow_gold` linear RGB
     **`[0.56, 0.43, 0.075]`**) and stronger golden mix weights:
     terrain golden mix `clamp(0.56 * D * F, 0, 0.75) * w`, meadow golden mix
     `clamp((0.14 + 0.48 * D) * F, 0, 0.78)` on both `BSDF_PRINCIPLED` and
     `BSDF_TRANSLUCENT`.
   - Drive explicit luma contrast between sunlit golden patches (`F`) and
     deeper green troughs (`T`) plus fine 0.28 m micro-contrast (`Micro` mapped
     with sharpened smoothstep `0.38..0.62`):
     - On meadow masters: macro-patch luma factor
       `(1.0 - 0.22 * T) * (1.0 + 0.32 * D * F)` multiplied by 3 m `Macro`
       (`0.80..1.22`) and 0.28 m `Micro` (`0.76..1.26`).
     - On exterior terrain (gated by `w = v13_exterior_weight`, leaving core
       and shaded forest untouched): macro-patch luma factor
       `(1.0 - 0.24 * T) * (1.0 + 0.36 * D * F)` multiplied by 3 m `Macro`
       (`0.78..1.24`) and 0.28 m `Micro` (`0.84..1.18`), with exterior terrain
       micro-bump strength `0.22`, distance `0.012 m`.
   - Calibrate these config-driven coefficients so that in the cold render
     `C_v16_c01_960.png`:
     - `Front meadow` luma std is in **`10.2–16.0`** and high-pass RMS is
       **`≥ 6.3`**;
     - `Left slope` luma std is **`≥ 5.5`** and `Right slope` luma std is
       **`≥ 7.8`**;
     - Golden pixel fraction (`R/G > 0.99`, `G/B > 1.35`, `luma > 80`)
       increases substantially over V15 C in **all three** meadow/slope crops
       (including a clearly non-zero golden fraction on the left slope and
       vivid golden-green accents on the right slope and front meadow), without
       garish yellow blotches or contour banding.
2. **Visibly soft, irregular gravel-trail edges and `0.45–0.75 m` vegetated shoulders:**
   - Preserve the central travelled gravel core (`abs(lateral) <= core_half(s)`,
     minimum full core width `0.84–0.96 m`) while making the visible gravel-to-grass
     edge wave organically **inside** the outer margin of `V07_TRAIL_MESH` so
     the 15 mm mesh boundary is completely dissolved into the surrounding
     meadow:
     - Let `Eσ(s) = h(s) - a(s) * (0.14 + 0.22 * Nedgeσ(s))` (clamped so the
       travelled gravel core width `E_left(s) + E_right(s)` is always at least
       `0.84 m`), with multi-scale edge wavelengths (`2.2 m` and `7.5 m`, plus
       a fine `0.65 m` 3D shader edge-noise perturbation `±0.08 m` on `d` in
       `V16_TRAIL_SHOULDER_FIELDS`).
     - Keep the stored shoulder width `Wσ(s) = 0.45 + 0.30 * Nwidthσ(s)` within
       **`[0.45, 0.75] m`** (`2 μm` tolerance).
     - In `V16_TRAIL_SHOULDER_FIELDS`, blend gravel → worn loam → local V16
       meadow/terrain green **across the outer margin of `V07_TRAIL_MESH`
       itself** (`Loam` ramp over `d ∈ [-0.08, 0.05] m`, and `Grass` ramp
       starting at `d = -0.02 m` and reaching `0.85–1.0` by the physical mesh
       edge `abs(lateral) = h(s)` and continuing smoothly across `Wσ(s)` on the
       terrain, using the same golden/macro/micro V16 meadow-substrate shading
       on the grass portion of `MAT_V16_V07_GRAVEL`). This eliminates the sharp
       high-contrast luminance step at `abs(lateral) = h(s)` and widens the
       measured foreground trail-edge transition ratio to **`≥ 1.25x`** C.
   - Make the low shoulder tufts visibly read at `960 × 540` while keeping full
     physical support:
     - Size the 8 complete-component shoulder masters to heights
       **`0.12–0.24 m`** and radial spread **`0.10–0.14 m`** (still `≤ 192`
       render triangles and `≤ 24` working triangles per master, dedicated
       `IsViewport` switch, working stride 4).
     - Allow shoulder tufts in `0.01 m < d < Wσ(s)` to root on **either**:
       (a) the actual terrain surface (`not gravel.hits(root_box)`), **or**
       (b) the outer green-blended margin of the `V07_TRAIL_MESH` top surface
       itself (where every basal vertex of `root_box` projects strictly onto
       `V07_TRAIL_MESH` top triangles with `abs(lateral) <= h(s) - 0.015 m` and
       `d >= 0.01 m`, so no root box ever bridges the 15 mm gravel lip!).
       Verify exhaustive basal support against whichever surface class (`terrain`
       or `trail_top`) supports that tuft (`exposure ≤ 1 mm`, `burial ≤ 18 mm`,
       `support span ≤ 5 mm`), while keeping zero intrusion into the travelled
       gravel core (`d <= 0.01 m`) and zero obstacle intersections.

## Authority and mutation axes

Positive authority / exact changed-path allowlist:
- New `R/work/v16/meadow_trail_01/source/meadow_trail_v16_c01.py`
- New `R/work/v16/meadow_trail_01/source/meadow_trail_v16_c01.json`
- New `R/work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16_c01.blend`
- New `R/work/v16/meadow_trail_01/renders/C_v16_c01_960.png`
- New `R/work/v16/meadow_trail_01/worker/c01_*`
- New `R/work/v16/meadow_trail_01/proofs/c01_*`
- New `R/work/v16/meadow_trail_01/runtime/c01_*`
- Direct-write terminal report `T/01_report_02.md`

Negative authority:
- Preserve all 01/02 deliverables (`candidate_exterior_v16.blend`,
  `B_v16_960.png`, `meadow_trail_v16.py`, `meadow_trail_v16.json`, existing
  `proofs/`, and `01_report_01.md`) byte-identically.
- Preserve all immutable V14/V15 inputs and all tracked project files.
- Same strict isolated CPU4 execution route and guards as 01/02 (no live MCP,
  no touching owner GUI PID 2452 / start_ticks 12233, serialized build →
  fresh-input replay → cold reopen & 960×540 render, start ≥12 GiB available
  RAM, own RSS ≤8 GiB / early-stop 7 GiB, available RAM ≥6 GiB, render time
  `<157.5 s`, 240 s watchdog).
- No Git writes, no network/downloads, no UHD render, no closure signal.

Repository mutation: only the new `c01` paths under `R/work/v16/meadow_trail_01/` listed above
Host/remote mutation: only owned isolated headless Blender child processes using `R/work/v16/meadow_trail_01/runtime/c01_*`; zero persistent host or remote mutation
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/01_report_02.md`

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
Downloadable prompt filename: 01_correction_02.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16
Report filename: 01_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Validation and completion contract

- Run the three serialized CPU4 children (`c01_build`, `c01_replay`,
  `c01_cold_render`) with the already corrected cross-process `/RNG` exclusion
  in the semantic comparison harness.
- Prove all preservation, idempotence, replay, cold reopen, 87-image
  portability, six `_working_branch` checks, and exhaustive basal support &
  hull clearance on `candidate_exterior_v16_c01.blend`.
- Compute the full fixed-crop and trail-edge comparison table across
  `C_v16_c01_960.png`, `B_v16_960.png` (01/02), V15 C, V15 B, and `01.png`, and
  directly inspect `C_v16_c01_960.png`.
- If thesame assumption or any required threshold still fails after this single
  correction, report `Status: PARTIAL` with
  `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`; if all technical and
  visual review gates pass, report `Status: PASS` and
  `Phase-qualified result: implementation-PASS`.
- Begin `T/01_report_02.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`,
  echo coordinates (`kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16`,
  `01`, `03`), include the compact core, verify full readback and SHA-256, and
  stop.

Authority expiry: this terminal report ends the `c01` correction grant; no
autonomous continuation, second correction, UHD render, publication, or closure
follows.
