# Diagnostic 01/06 — Saved v005 state verification

Delivery marker: **TEN ISTÝ CHAT**
Actual client mode: **Cursor Agent mode; native Plan mode OFF** (`not-used`)
Persistent role identity: WORKER
Worker session profile: Diagnostic Worker
Phase: Diagnostic Closeout
Task identity: `JELENA-ACCESS-PATH-GRAVEL-PARKING-SAVED-STATE-CHECK`
Delivery route: manual Cooperator delivery
Reasoning recommendation: **Standard/Medium** — one bounded saved-file readback and comparison; no design work.
Recommended context capacity: approximately 250k tokens — a recommendation, not observed telemetry or a token cap.
Requested model: Michal's current Cursor model selection; effective model identity unverified.

Continuity anchor: the implementation-PASS report `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_04.md` and candidate commit `0ce1917386a1de0fb8ef7afb481fda0838683f0e`.
Authority renewal: prior implementation authority expired at `01_report_04.md`; this exchange grants a bounded load-and-readback diagnostic only.
Why current-session reuse: the same session holds the implementation context and the exact candidate identity; independence is not required.
Retained context: convenience, not authority. Re-gate from the saved file and repository evidence.
Evidence posture: non-independent diagnostic evidence.

```text
Logical whole identity: jelena-access-path-and-gravel-parking
Worker session ordinal: 01
Worker exchange ordinal: 06
Implementation authority: none
Native planning mode: not-used
Worker session target: current-worker-session
Exact baseline: candidate commit 0ce1917386a1de0fb8ef7afb481fda0838683f0e; Jelena/Jelena_Realistic_v005.blend SHA-256 77ef85368c6768328552b1c844df16c3de86c2ce137b22c145176b64c38a0f04; Jelena/Jelena_Realistic_v004.blend SHA-256 00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa
Changed-path allowlist: /Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_05.md
Implementation boundaries: no scene construction, no render, no save, no Git write; only open the saved v005 from disk and read back its state
Independence required: no
```

## Why this check exists

The candidate was reported as implementation PASS and committed. The post-report live session is `Jelena_Realistic_v005.blend` with `bpy.data.is_dirty = true`. In the live session, Camera A was read at world translation `(4.2829, 24.2327, 6.35)` and Camera D at `(13.638, 27.473, 15.5)`, which do not match the report and manifest values `(13.9, -16.4, 6.35)` and `(7.0, -23.5, 15.5)`. The evidence images show the original Camera A framing and the planned overview, so the saved file may still be correct and the live camera moves may be unsaved inspection changes.

Do not trust either state. Open the saved candidate from disk and verify what is actually committed.

## Authorized operation

Open exactly:

```text
/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v005.blend
```

Use `bpy.ops.wm.open_mainfile(filepath=...)` or the verified Slovak `Súbor → Otvoriť` flow. Opening the saved file is authorized; it discards the current unsaved live camera/settings changes, which are not the candidate and not owner work. Do **not** save before opening. Do **not** save after opening unless a later explicit correction grant authorizes it.

Before opening, verify the file exists and its SHA-256 is `77ef85368c6768328552b1c844df16c3de86c2ce137b22c145176b64c38a0f04`. If it differs, stop and report.

## Readback checks

After opening, record and compare:

1. `bpy.data.filepath`, `bpy.data.is_dirty`, active scene, active camera, frame.
2. Camera A `matrix_world`, location, rotation, lens, sensor fit, sensor dimensions, shift. Expected original: world translation `(13.9, -16.4, 6.35)`, rotation Euler `(1.390952, 0.0, 0.477129)`, lens `46 mm`, sensor `36 × 24`, shift `0/0`.
3. Camera D `D • Prístup zhora`: location `(7.0, -23.5, 15.5)`, lens `28 mm`, sensor `36 × 24`, and its world matrix/aim.
4. Saved render settings: `1260 × 840`, samples `80`, denoise off, colour mode `RGBA`, `use_border` and `use_crop_to_border` off, camera A active.
5. Scene A and scene B object counts; scene B must be `308`.
6. Collections `05b • Nášľap • ponechané`, `05c • Vegetácia • odstránená pre prístup`, `10a • Vegetácia • mimo prístup`: view-layer `exclude = true`. `11 • Prístup • A`, `11a • Pomocné • A`, `07d • Kamera prístup • A` present.
7. `Proxy • auto` and `Maska prístupu` have `hide_render = true`.
8. The three hidden objects are in `05c`; the 20 `Nášľap` objects are in `05b`; `Kameň` has `25` users.
9. The candidate file hash after opening is unchanged; `v004` on disk remains `00d1...`.
10. No new collection or object is linked into scene B.

Do not re-render. Do not compare pixels. Do not rebuild anything. The purpose is saved-state identity.

## Authority and trace

Positive authority: read-only repository/file metadata, opening the exact saved v005 once, and reading its scene state; exact report write below.

Negative authority: no scene construction, no render, no save, no Save As, no file replacement, no Git fetch/stage/commit/push, no .local writes, no external assets, no credentials, no host changes, no acceptance/publication/closure.

Repository mutation: none
Host/remote mutation: none
Trace persistence: direct-write `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking/01_report_05.md`

Cooperator delivery / trace destination: configured
Downloadable prompt filename: `01_diagnostic_05.md`
Destination path: `/Users/agile/meta/projects/jelena/00/03-jelena-access-path-and-gravel-parking`
Report filename: `01_report_05.md`
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Report contract

The report must begin exactly `### Report for ORCHESTRATOR_CHAT` and echo coordinates `01`/`06`.

Include:

- `status: PASS | PARTIAL | BLOCKED`
- `Phase-qualified result: not-applicable`
- `Start commit:` and `End commit:` both `0ce1917386a1de0fb8ef7afb481fda0838683f0e` if no repository mutation
- `Report justification: new-evidence`
- `Logical-whole closure: not-closed`
- The exact saved-file hash and the readback values for Camera A, Camera D and render settings.
- A clear verdict: the saved candidate matches the report/manifest, or the exact mismatches.
- Scene B, collections, hidden objects, stones, `Kameň`, proxy and mask results.
- A statement that the unsaved live camera/settings changes were discarded by opening the saved file, and that the file on disk was not saved or rewritten.
- Any limitation or mismatch. Do not repair it in this exchange.
- `Orchestration critique:` with MEASURED and LEAD.
- `Resolved Execution Issues / Near-Misses:` none or complete.
- `Authority expiry:` terminal report ends the grant.

PASS means the saved candidate was opened and every checked value matches or an exact, non-blocking limitation is named. PARTIAL means the check is incomplete. BLOCKED means the saved file cannot be opened or its identity cannot be established.

Do not claim acceptance, publication PASS or closure. Do not emit the closure signal.
