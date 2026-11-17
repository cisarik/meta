# Interruption record — Worker session 05, exchange 01

Author: ORCHESTRATOR (not the Worker). Written 2026-11-17 23:08 from
observed facts; no terminal Worker report exists for this exchange.

Logical whole identity: kysucka-moderna-chata-interior-living-space
Worker session ordinal: 05
Worker exchange ordinal: 01
Prompt: `05_implementation_00.md`, SHA-256
`72e77932ebb5651f2d3cf9c395306449316ffcaecba034cb06f2d0c038fdd45a`
Trace companion outcome: interruption

## What happened

- Issued about 22:19 to a fresh write-capable subagent session.
- The session worked until 22:47:10 (last file) / 22:47:38 (last transcript
  record). It wrote no report.
- The client ended the turn with the error
  `Other Models usage limit reached. Switched to Auto after reaching Other
  Models usage limit.` No Worker acknowledgement exists. No Blender process
  of this session was running at 23:07; the empty `work/v10/run_job.lock`
  holds no lock (the launcher uses `fcntl`, and the file being present does
  not block the next run).

## Work product (unaccepted)

Slice 1 is preserved under `work/v10/slice1/` with the hashes from exchange
04/01, including the module `9403c82f…`, the study scene `c63ddb25…` and
the nine renders.

Slice 2, as left at 22:47 (SHA-256):

| File | SHA-256 |
|---|---|
| `scripts/interior_v10.py` | `45fc7513597d287b518aacf35d41169eefcbfdbf44804b2f700236ccb7d4e38d` |
| `scripts/interior_v10_study.py` | `f8c1a6d2fecf4d8de36e9e8674541d8485e3a7fce1d020f86b504cd5b5d29c70` |
| `model/interior_v10.json` | `c328f719a5c31edb26ad24dee7d83e5bc75cb6f3bf2cf48e71cb5630659c4a75` |
| `work/v10/run_job.py` | `686c071f59e0ff401b89aa586d8a39e6ce524d7e3962db216fa4c7e486db5c5c` |
| `work/v10/study/interior_study_v10.blend` | `4e4f73787be15c25f79e0ab9b37545bd61dc52a95c9f7ee793472cc07e0f2816` |
| `assets/interior_v10/` | 293 MB, `MANIFEST.md` present, CC0 Poly Haven |

`work/v10/evidence_s2/checks.json` from job `s2_03_check` (exit 0, 10.8 s,
2.2 GiB): geometry, idempotence, protected witnesses, saved-scene witness,
camera framing and textures passed. These three did not:

- `c1_visibility`: the ray to the stair landing hits `V10_ARMCHAIR` at
  (13.836, 1.504, 1.263). The other four rays pass.
- `collisions`: gallery ottoman intersects three plants (up to 0.18 m);
  a plant clips the railing by 5 mm; the kitchen base meets the tall unit
  with 5 mm overlap; the front frame enters `SOFFIT_wood_0` by 0.15 m.
- `routes`: `V10_KITCHEN_BASE` enters the kitchen-aisle box by 4 mm
  (y 7.446 against the box edge 7.45). The other four routes pass.

No slice 2 render exists. The cold-open check was not run. Assets were not
re-verified by the Orchestrator beyond the manifest's presence and the
directory size.

## Disposition

Coordinates 05/01 are consumed and that grant's authority has ended. The
files above are unaccepted work of an interrupted exchange. The same slice
continues under a new complete grant to a fresh session (06/01): repair the
three failing checks, then render. Assets are not downloaded again.

After this record, the Orchestrator corrected a wrong timestamp in
`evidence/design_basis_v10.md` (the heading of Amendment 2). The file's
SHA-256 is now
`4901cdc0da78c5cb7b64992ee3eaa76bc5d3885d7b90f1e730b2be3bc40a2870`.
Nothing in the amendment's decisions changed.
