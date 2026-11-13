# Owner-Feedback Correction 01/07 — Jelena paved access and gravel parking

Delivery marker: **TEN ISTÝ CHAT**
Actual client mode: **Cursor Agent mode; native Plan mode OFF** (`not-used`)
Persistent role identity: WORKER
Worker session profile: Bounded Correction Worker
Phase: Implementation correction
Task identity: `JELENA-ACCESS-PATH-GRAVEL-PARKING-OWNER-CORRECTION`
Delivery route: manual Cooperator delivery
Reasoning recommendation: **High** — the correction changes the parking material, the path-to-parking junction and the review camera set while preserving the accepted scene and render budget; Medium cannot safely resolve those interactions.
Recommended context capacity: approximately 250k tokens — a recommendation, not observed telemetry or a token cap.
Requested model: Michal's current Cursor model selection; effective model identity unverified.

Continuity anchor: implementation report `01_report_04.md`, saved-state diagnostic `01_report_05.md`, candidate commit `0ce1917386a1de0fb8ef7afb481fda0838683f0e`, and the owner’s 2026-11-13 visual feedback on `evidence/access-005/overview.png`.
Authority renewal: prior implementation/diagnostic authority expired; this exchange grants one bounded owner-feedback correction.
Why current-session reuse: the same healthy session holds the candidate, the manifest and the exact scene state; independence is not required.
Retained context: convenience, not authority. Re-gate from the saved candidate and repository evidence.
Evidence posture: non-independent implementation evidence.

```text
Logical whole identity: jelena-access-path-and-gravel-parking
Worker session ordinal: 01
Worker exchange ordinal: 07
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: candidate commit 0ce1917386a1de0fb8ef7afb481fda0838683f0e; Jelena/Jelena_Realistic_v005.blend SHA-256 77ef85368c6768328552b1c844df16c3de86c2ce137b22c145176b64c38a0f04; Jelena/Jelena_Realistic_v004.blend SHA-256 00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa
Changed-path allowlist: Jelena/Jelena_Realistic_v005.blend; scripts/access_landscape_v005.py; evidence/access-005/camera-a-after.png; evidence/access-005/overview.png; evidence/access-005/camera-a-terrace-detail.png; evidence/access-005/overview-bok.png; evidence/access-005/top-view.png; evidence/access-005/connection-detail.png; evidence/access-005/parking-detail.png; evidence/access-005/path-a-view.png; evidence/access-005/manifest.json; deletion of evidence/access-005/camera-a-detail.png; .local/checkpoints/Jelena_Realistic_v005-before-owner-correction.blend (untracked checkpoint, never staged)
Implementation boundaries: one bounded correction only — dark gravel parking, path B end flare and dark gravel apron, five new review views, replacement of the occluded side detail; preserve the accepted layout, cabin, terrace, furniture, steps, Camera A/D, lighting, scene B, trees and all protected baselines
Independence required: no
```

## Owner findings

Michal reviewed `evidence/access-005/overview.png` and reported:

1. The other evidence images do not show the access; more renders from different angles are needed.
2. The path B connection to the road/parking is not convincing enough.
3. The parking should use black/dark gravel so it is visually prominent, and the parking area should be filled with it.

These are concrete correction findings. They do not reopen the objective. Keep one coherent access landscape.

## The bounded correction

### 1. Dark gravel parking

Split the current shared road/parking material:

- `Cesta • lesná` — light warm grey-brown compacted forest road; keep the road relatively light, roughness about `0.86`, subtle noise and fine bump.
- `Parkovanie • čierny štrk` — dark charcoal/black aggregate, base colour about `(0.02, 0.02, 0.02)` to `(0.06, 0.055, 0.05)`, roughness about `0.88`, Voronoi scale about `22`, noise scale about `4`, bump `0.20`. It must read as gravel, not a black hole or asphalt.
- Wheel strips `0.28 m` wide on `1.50 m` centres, slightly lighter compacted grey-brown (`0.07–0.10`), strongest on the stall, faded over the tapers.
- Assign `Cesta • lesná` to `Cesta • les` and `Parkovanie • čierny štrk` to `Parkovanie • štrk`.
- Fill the entire parking footprint and its tapers with the dark gravel. No bare terrain, light patches or gaps inside the parking. Keep the road material light so the dark pull-off is prominent.

Do not change the parking footprint, road centreline, car proxy, wheel-strip geometry or stall dimensions.

### 2. Path B to parking/road connection

Keep the path B centreline and its `1.20 m` width for the main run. Change only the last `0.80 m` at the parking end:

- flare the paver field from `1.20 m` to about `1.60 m`;
- keep the paver top easing from `70 mm` to `12 mm` over that last `0.60–0.80 m`;
- add a dark gravel transition apron `Prechod • štrk`, about `1.80 m` wide and `0.80 m` deep, centred on the path end, overlapping the parking by about `0.60 m`; use `Parkovanie • čierny štrk`;
- the pavers must meet the apron and the parking with no gap, lip, floating edge or grass wedge;
- extend the grass mask to cover the flare and apron with the same `0.12 m` margin;
- keep the path B connection to `Schod terasy.003` unchanged.

The result should read as paving entering the dark gravel pull-off, and the pull-off connecting to the road, not a path ending at an unrelated light apron.

### 3. New review views

Add five scene-A-only cameras in a new collection `07e • Kamery • hodnotenie • A`. Camera A and Camera D must not move. Approximate values, with a small framing allowance:

| Camera | Purpose | Location | Lens | Aim |
|---|---|---|---|---|
| `E • Prístup • bok` | low three-quarter view of road, parking, path and steps | `(-7.0, -20.0, 9.0)` | 30 mm | `(5.5, -7.5, -0.2)` |
| `F • Prístup • pôdorys` | orthographic layout view | `(5.0, -7.0, 30.0)`, rotation `(0,0,0)` | ortho scale about `32 m` | down |
| `G • Napojenie • detail` | path B flare, apron, parking and road edge | `(2.5, -6.0, 3.5)` | 35 mm | `(5.6, -9.4, -0.2)` |
| `H • Parkovanie • detail` | dark gravel, wheel wear, stall and road edge | `(7.5, -5.0, 4.0)` | 35 mm | `(8.3, -10.5, -0.2)` |
| `I • Chodník A • detail` | side path A from entry to last stone, joints and east gap | `(9.5, 4.5, 4.5)` | 35 mm | `(11.2, -0.9, -0.2)` |

Framing allowance: up to `3 m` translation and `5 mm` lens adjustment per camera, plus ortho scale `28–36 m` for the top view, only to fit the required content. Record final transforms. If `I • Chodník A • detail` cannot avoid the foreground needles from any allowed position, report the limitation; do not add another camera outside this set.

### 4. Evidence set

Replace the occluded side detail:

- delete `evidence/access-005/camera-a-detail.png` with `git rm`; Git history preserves it.
- add `evidence/access-005/path-a-view.png` from camera `I`.

Final retained evidence set:

```text
camera-a-before.png          (unchanged, from v004)
camera-a-after.png           (re-render from corrected v005)
overview.png                 (re-render from corrected v005, camera D)
camera-a-terrace-detail.png  (re-render from corrected v005)
overview-bok.png             (new, camera E)
top-view.png                 (new, camera F)
connection-detail.png        (new, camera G)
parking-detail.png           (new, camera H)
path-a-view.png              (new, camera I)
manifest.json                (updated)
```

All after/detail/overview images must come from the corrected v005. The before image stays from v004. Do not reuse an image from the pre-correction candidate.

Matched Camera A recipe stays `840 × 560`, 32 samples, adaptive threshold `0.01`, min `0`, OpenImageDenoise, seed `0`, AgX, look None, exposure `0`, gamma `1`, sRGB, PNG RGB 8-bit, frame 1, Cycles CPU. Overview and new views use the same engine/samples/colour. Top view is orthographic. Restore the saved `1260 × 840 / 80 samples / denoise off / RGBA / border off` settings before the final save.

Budget: eight new final renders in this correction; up to four additional low-sample framing tests; cumulative render wall-clock at most `15` minutes; no animation. Stop/simplify at `4.5 GiB` sampled RSS; never exceed `6.0 GiB`. Record sampled RSS in KiB and state it is not peak memory.

## Preservation

- Do not move Camera A or Camera D; do not change their lens/sensor/shift.
- Do not change the cabin, terrace, furniture, steps, lighting, world, colour management or scene B.
- Do not change the road centreline, parking footprint, stall dimensions, path B centreline, path A route or tree hides.
- Keep `05b` stones, `05c` hidden vegetation and `10a` excluded vegetation unchanged.
- `Kameň` remains 25 users and untouched.
- New cameras are scene-A-only; scene B remains 308 objects with no new collections.
- No whole-scene vegetation generator; only the existing local `Pokryv lesa` mask is extended for the flare/apron.
- No external assets.

## Checkpoint and sequence

1. Preflight: live filepath `Jelena_Realistic_v005.blend`, `is_dirty false`, scene A, camera A, frame 1, scene A 931, scene B 308, Camera A and D at the saved values, v005 hash `77ef...`, v004 hash `00d1...`, `05b/05c/10a` excluded, proxy/mask hidden. Stop on any mismatch.
2. Confirm `.local/checkpoints/Jelena_Realistic_v005-before-owner-correction.blend` is absent, copy current v005 there, hash both. Both must equal `77ef...`. Never stage the checkpoint.
3. Modify the materials, path B end flare/apron, mask and new cameras. Extend `scripts/access_landscape_v005.py` or add a clearly named correction script; the existing script/path is allowlisted. The script must not rebuild the whole scene, move trees, change layout or touch Camera A/D.
4. Save corrected `v005`; hash it.
5. Render the evidence set. Inspect actual images. Use framing tests as needed; do not change the specified material/layout correction except one bounded framing adjustment.
6. Update `manifest.json` with the new candidate hash, all image hashes, settings, camera transforms, scene-B count, `Kameň` users, hidden objects, proxy/mask, render seconds, sampled RSS and visual review.
7. Remove `camera-a-detail.png` from Git and the manifest; add the new images.
8. Verify preservation and hash `v004` again.
9. Stage only the exact commit paths; commit and push ordinarily non-force; verify the public ref.
10. Write `01_report_06.md`.

## Git authority

Stage only:

```text
Jelena/Jelena_Realistic_v005.blend
scripts/access_landscape_v005.py
evidence/access-005/camera-a-after.png
evidence/access-005/overview.png
evidence/access-005/camera-a-terrace-detail.png
evidence/access-005/overview-bok.png
evidence/access-005/top-view.png
evidence/access-005/connection-detail.png
evidence/access-005/parking-detail.png
evidence/access-005/path-a-view.png
evidence/access-005/manifest.json
```

Plus the exact deletion of `evidence/access-005/camera-a-detail.png` via `git rm`. The unchanged `camera-a-before.png` and `README.md` stay untouched and unstaged. Never stage `.local` checkpoints or the Meta report.

One commit, message:

```text
Refine the gravel parking and path connection, add review views.

The dark gravel pull-off and flared path junction make the access legible from the new review angles.
```

One ordinary non-force `git push origin HEAD`; verify `git ls-remote origin refs/heads/main`. No fetch/pull, no force, no LFS, no history rewrite. If the push is rejected, stop.

## Authority and trace

Positive authority: read-only inspection; exact scene-A correction; checkpoint copy; opening/saving the candidate; renders and evidence writes; manifest; one Git commit/push; exact report write.

Negative authority: no layout, cabin, terrace, furniture, steps, Camera A/D, lighting, world, colour-management, scene-B, tree or vegetation-hide changes; no road/parking/path centreline or footprint change; no whole-scene regeneration; no external assets; no credentials; no host changes; no LFS/force/history rewrite; no Meta Git; no acceptance/publication/closure; no subagents or parallel work.

Repository mutation: `Jelena/Jelena_Realistic_v005.blend`; `scripts/access_landscape_v005.py`; `evidence/access-005/camera-a-after.png`; `evidence/access-005/overview.png`; `evidence/access-005/camera-a-terrace-detail.png`; `evidence/access-005/overview-bok.png`; `evidence/access-005/top-view.png`; `evidence/access-005/connection-detail.png`; `evidence/access-005/parking-detail.png`; `evidence/access-005/path-a-view.png`; `evidence/access-005/manifest.json`; deletion of `evidence/access-005/camera-a-detail.png`; `.local/checkpoints/Jelena_Realistic_v005-before-owner-correction.blend` (untracked, never staged)
Host/remote mutation: ordinary non-force push to `origin` `refs/heads/main` at `https://github.com/cisarik/jelena`
Trace persistence: direct-write `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_06.md`

Cooperator delivery / trace destination: configured
Downloadable prompt filename: `01_correction_06.md`
Destination path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Report filename: `01_report_06.md`
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR (Meta Git); project Git push is separately authorized above
Archival: wait-for-report

## Report contract

The report must begin exactly `### Report for ORCHESTRATOR_CHAT` and echo coordinates `01`/`07`.

Include:

- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: implementation-PASS | not-applicable`
- `Start commit:` `0ce1917386a1de0fb8ef7afb481fda0838683f0e`
- `End commit:` the new commit
- `Report justification: new-mutation`
- `Logical-whole closure: not-closed`
- Changed files, new candidate SHA-256, checkpoint SHA-256, script SHA-256, manifest SHA-256.
- The exact parking material values and path B flare/apron dimensions built.
- New camera transforms and image paths/dimensions/hashes/render seconds.
- Preservation results: Camera A/D, scene B 308, `Kameň` 25, stones, hidden objects, proxy/mask, no tree moves.
- Performance: total render seconds, sampled RSS in KiB (not peak).
- Git commit/push and public-ref verification.
- Image inspection findings; known limitations.
- A short numbered acceptance request focused on the dark parking, the path connection, the new views and the east gap.
- `Orchestration critique`, `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`.
- No acceptance, publication PASS or closure claim; authority expiry.

PASS means the correction and evidence set are complete and preserved. PARTIAL means a named required view or check is missing. BLOCKED means a prerequisite prevents the correction.

## Stopping conditions

Stop and report if:

- live v005 is not clean, not the expected candidate, or Camera A/D differ from the saved values;
- v005 hash differs or the v005 checkpoint already exists;
- a required change would move Camera A/D, trees, layout, parking footprint or scene B;
- another object blocks the path connection or the new views cannot show the required content within the framing allowance;
- render budget, wall-clock or RSS gate is exceeded;
- Git would require force, LFS or a path outside the allowlist;
- any external asset, credential or host change is required.

Do not claim acceptance, publication PASS or closure. Do not emit the closure signal. Authority expires at the terminal report, cancellation or supersession.
