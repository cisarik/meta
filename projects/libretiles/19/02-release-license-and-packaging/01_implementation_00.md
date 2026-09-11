You are a WORKER instance assigned to the persistent AP WORKER role. Perform exactly this bounded IMPLEMENTATION task and stop.

```text
Logical whole identity: release-license-and-packaging
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task identity: LIC-IMPL — add MIT LICENSE file, license fields to package manifests, and minimal CHANGELOG skeleton. One commit. Closes G12 (missing LICENSE) and the packaging metadata from the triage plan.
Phase: Implementation
Implementation authority: explicit
Exact baseline: c00be7cb4bbaaf086dede3901461a06dee5308e1
Independence required: no
Evidence posture: non-independent
Evidence tier: E0
Evidence tier basis: metadata additions only; zero executable path, zero test change, zero production code, zero CI.
Repository checkout topology: standalone checkout
Logical-whole closure: not-closed
```

```text
Changed-path allowlist:
  /home/agile/Projects/libretiles/LICENSE       (NEW file)
  /home/agile/Projects/libretiles/CHANGELOG.md  (NEW file)
  /home/agile/Projects/libretiles/frontend/package.json
  /home/agile/Projects/libretiles/backend/pyproject.toml
```

## Changes

**LICENSE** (new root file) — standard MIT license text:

```
MIT License

Copyright (c) 2025-2026 Libre Tiles contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**CHANGELOG.md** (new root file) — minimal skeleton:

```md
# Changelog

## 2026-09-10

- test(parity): re-pin persisted move payload to the canonical inspection shape
- test(replay): reconcile admin replay fixture to AT/4 story
- fix: update judge docstring Tier-2 status and add Node engines field
- feat: initial changelog, MIT license file, and packaging metadata
```

(Nothing else to list — this is the first tagged release note.)

**frontend/package.json** — add `"license"` field after `"private": true`:

```json
  "license": "MIT",
```

**backend/pyproject.toml** — add `license` field after `version = "0.1.0"`:

```toml
license = "MIT"
```

READ verification: `README.md:207` already says "MIT". `libretiles_PRD.md:146` already says "- MIT license." No changes needed in either file.

## Work sequence

1. Repository gate: HEAD = `c00be7cb4bbaaf086dede3901461a06dee5308e1`, AP `9c5cc44f`, porcelain empty, branch main.
2. Create LICENSE, CHANGELOG.md; edit package.json, pyproject.toml.
3. `git diff --stat` — 4 files.
4. Validation:
   - `npm run typecheck` — clean
   - `npm run lint` — clean
   - `npm run build` — exit 0
   - `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/pytest backend/tests/test_documentation_deployment_claims.py -q` — the five-gate doc-claims module green (fast). Full backend pytest unchanged from green S3 suite: skip unless you want to re-verify; report as "full pytest not re-run (metadata-only; last known green at c00be7c with 1243 passed)".
5. Commit + non-force push: `chore: add MIT license, changelog skeleton, and packaging license metadata`. Push. `git ls-remote origin refs/heads/main` must match.

## Authority

```text
Filesystem: create LICENSE + CHANGELOG.md; edit package.json + pyproject.toml. /tmp/opencode/lic/ for temp.
Git: stage/commit/push non-force. Network: push + ls-remote only. No secrets, deps, docker.
```

## Report contract

Begin `### Report for ORCHESTRATOR_CHAT`. Echo the coordinates unchanged:

```text
Logical whole identity: release-license-and-packaging
Worker session ordinal: 01, Worker exchange ordinal: 01
```

status: PASS|PARTIAL|BLOCKED, Phase-qualified result: implementation-PASS, commit, changed files, gates, Report justification: new-mutation, authority expiry, context pressure.