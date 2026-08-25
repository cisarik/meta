### Report for ORCHESTRATOR_CHAT

Echoed coordinates:

```text
Logical whole identity: framenest-public-published-surface-and-tailscale-workspace
Worker session ordinal: 05
Worker exchange ordinal: 03
```

Worker session target: `current-worker-session` (same healthy session 05).
Native planning mode: not-used. Continuity anchor: exchange 02 terminal report;
HEAD `be35922d223c49f3b140453e69b313c9086c3831`. Authority renewal: complete new
bounded grant; exchange 02 authority expired at its terminal report.

**Capability handshake:** opencode CLI agent on Linux/bash (directly observed);
model label self-reported, not independently verifiable. This exchange:
read-only git inspection only; zero repository mutation; zero Python/test/ap
exec/network/NUC/SSH/sudo/provider/browser invocations. Precondition gate
passed: HEAD = declared baseline exactly, worktree clean. Allowlisted write
path used once, at the Orchestrator-corrected location (`framenest`, not the
transcribed `framenet`). Command verification performed before writing: entry
points read from `pyproject.toml:10`; launcher behavior from
`DEVELOPMENT.md:56-60`,`:110-124` and
`src/framenest/infrastructure/runtime/development.py:40`,`:470`; all three infosec
script interfaces re-checked from their own headers plus live `-h`
invocations via `bash <script>`; every file:line cited below re-grepped at
HEAD.

**Non-blocking observation for the Orchestrator:** the three
`scripts/operator/infosec/*.sh` files were committed without the executable
bit (exchange 02 invoked them through `bash <script>`). All commands in this
guide therefore use the explicit `bash scripts/operator/infosec/…` form, which
works everywhere. Separately, explicit `-h` currently falls through to the
normal run path instead of exiting 0 after printing usage. Both are one-line
fixes; they need their own bounded task — no authority exists in this exchange.

---

# Cooperator acceptance-test guide — dual-audience boundary & infosec hardening

Michal, this guide lets you verify with your own eyes what this logical whole
shipped, before Orchestrator closure. Work top to bottom. Nothing here
requires the NUC until Part B, and Part B itself is honestly conditional —
see its banner.

**What changed in this whole** (commits `37da5f2..be35922`, one line per
rollout):

| Commit | Rollout |
|---|---|
| `0008ca5`+`6aac705` | ADR-0074 proposed and accepted: dual-audience public/Tailscale boundary |
| `ffef457`+`dd26782` | administrator publication became the sole publication write; unpublish added on that route |
| `95f514b` | local-only `public_published_uds` reader: separate app, read-only engine, GET-only allowlist |
| `5b99575` | contributor-scoped workspace media list + administrator contribution filter |
| `da06109` | durable ordinary-user analysis proposals (no provider execution) |
| `f59f401` | audited administrator team-alias reads |
| `bcf5ec1`→`3a21405` | independent-audit remediation: tcp loopback guard (F-2), uniform sanitized 404 + loud marker/logging failures (F-1/F-4/F-5), percent-encoded read-only URI (F-6), per-user hourly proposal rate limit (F-3) |
| `be35922` | `docs/INFOSEC.md` hardening manual + three read-only operator diagnostics |

---

## Part A — MacBook, local only (no NUC, no Tailscale)

All commands are Fish on your MacBook, run from the repository root. You need
the prepared environment once (`./framenest setup`) if you have not run this
repo lately.

### A0 — deterministic acceptance directory

Purpose: keep every artifact of this test in one place so the two processes
share one known database and you delete one directory at the end.

```fish
# [MacBook / fish]
set -x ACC $HOME/.cache/framenest-acceptance
mkdir -p $ACC/sockets
#------------------------------------------------------
```

Expected: directory created silently. Failure: `mkdir:` error means a stale
file occupies the path — remove `$ACC` and retry. Report: cite **A0**.

### A1 — start the workspace (trusted-loopback) server

Purpose: run the workspace composition locally on loopback with the catalog
migrated to schema head `0033`, using your acceptance database.

```fish
# [MacBook / fish]
cd ~/Projects/framenest   # adjust to your checkout path
set -x FRAMENEST_DATABASE_PATH $ACC/catalog.sqlite3
./framenest start --no-open
#------------------------------------------------------
```

Expected: launcher output ends with a successful health wait; the server is
detached. The launcher enforces host `127.0.0.1`, migrates to the packaged
Alembic head, and waits for `GET /health` (`DEVELOPMENT.md:119-124`).
Failure: any red traceback or non-zero exit — paste the launcher's final lines.
Report: cite **A1**.

### A2 — confirm the audience bootstrap grants the admin-grade local audience

Purpose: prove the local composition resolves to `trusted_loopback` with the
full administrator capability set, identity-absent
(`src/framenest/adapters/api/application.py:1357-1362`).

```fish
# [MacBook / fish]
curl -s http://127.0.0.1:8000/api/audience/me
#------------------------------------------------------
```

Expected JSON contains `"audience":"trusted_loopback"`, `"identity":null`,
and capabilities including `"metadata.canonical.write"`, `"media.content.publish"`,
`"analysis.propose"`.
Failure: anything else (404, empty body, different audience) — include the raw
response. Report: cite **A2**.

### A3 — workspace admin UX walk-through in the browser

Purpose: exercise, by hand, the four admin surfaces this whole shipped.

```fish
# [MacBook / fish]
open http://127.0.0.1:8000/
#------------------------------------------------------
```

Check, in order (UI anchors verified in source):

1. **Publish / Unpublish**: select one catalog item in Manage media and use
   the **Publish** button (label rendered at
   `src/framenest/adapters/api/web/app.js:8349`; batch confirm
   "Publish selected" at `app.js:9235-9238`). Then **Unpublish** it again
   (`Unpublish` controls exist per-item and in batch views,
   `app.js:1244`,`:8369-8425`). Leave exactly one or two items **published**
   for the public-reader steps.
2. **Contributor filter**: in the administrator media list, set the
   contributor filter control (strings present in
   `web/index.html`; API support `5b99575`) and observe the list narrowing.
3. **Team aliases panel**: open the **Team aliases** panel
   (`index.html:872`) on a published item with a user alias present; expect
   proposer/owner login identifiers only behind this audited admin view
   (`f59f401`). If you have no alias yet, skip and note "no data".
4. **Analysis proposals browser**: open the **Analysis proposals** browser
   (`index.html:61`,`:967`). It should show an empty or existing open-proposal
   list without errors.

Expected: every action returns visible success; no console errors.
Failure: screenshot + which numbered sub-step failed. Report: cite **A3.1**…
**A3.4**.

### A4 — create an analysis proposal twice (rate-limit evidence)

Purpose: see disposition B work end-to-end: duplicates are accepted up to the
per-user window limit, then honestly rejected with a sanitized 429
(`src/framenest/application/analysis_proposal.py:30`,`:77-88`).

```fish
# [MacBook / fish]
set MEDIA_ID <paste-the-published-media-id-from-A3>
for i in 1 2 3 4 5 6 7
    curl -s -o /dev/null -w "%{http_code}\n" \
        -X POST -H 'Content-Type: application/json' -H 'X-FrameNest-Request: 1' \
        -H "Origin: http://127.0.0.1:8000" \
        -d '{}' "http://127.0.0.1:8000/api/workspace/media/$MEDIA_ID/analysis-proposals"
end
#------------------------------------------------------
```

Expected: six lines `201`, then one `429` whose body is exactly
`{"error":{"code":"ANALYSIS_PROPOSAL_RATE_LIMIT","message":"Too many analysis proposals this hour."}}`
(run the last call once more without `-o /dev/null` to see the body).
Failure: seven 201s would mean the limiter is not wired — include the codes.
Report: cite **A4**.

### A5 — start the public reader on its own Unix socket

Purpose: run the second, separate composition exactly as designed —
`public_published_uds`, distinct socket, same database opened read-only
(`docs/INFOSEC.md` §3 table; dispatch at
`src/framenest/adapters/api/application.py:375-380`).

New terminal (keep A1 running):

```fish
# [MacBook / fish]
cd ~/Projects/framenest
set -x FRAMENEST_INGRESS_MODE public_published_uds
set -x FRAMENEST_UDS_PATH $ACC/sockets/public.sock
set -x FRAMENEST_DATABASE_PATH $ACC/catalog.sqlite3
poetry run framenest-server
#------------------------------------------------------
```

Expected: server starts and binds the socket; **no TCP port is opened**
(`src/framenest/server.py:29-30`). Failure: startup refusal naming the schema
head or missing catalog means A1 did not migrate `$ACC/catalog.sqlite3` —
recheck A0/A1 ordering. Report: cite **A5**.

### A6 — public page shows published items only

Purpose: confirm the free public origin answers with the redacted published
projection.

```fish
# [MacBook / fish]
curl --unix-socket $ACC/sockets/public.sock http://localhost/api/audience/me
curl --unix-socket $ACC/sockets/public.sock http://localhost/api/media | head -c 400
open -a Safari http://localhost # does not apply — see note below
#------------------------------------------------------
```

Note: a plain browser cannot reach a UDS; view the page through the scripted
check in A7, or optionally `socat TCP-LISTEN:8443,range=127.0.0.1/32,fork UNIX-CONNECT:$ACC/sockets/public.sock`
in a third terminal and open `http://127.0.0.1:8443/` (skip if you do not have
socat — the curl evidence is sufficient).

Expected: `/api/audience/me` reports `"audience":"public_published"` with
capabilities exactly `["gallery.read","media.original.read"]`; `/api/media`
lists only what you published in A3, with no internal fields.
Failure: unpublished item visible, or extra fields — capture the JSON.
Report: cite **A6**.

### A7 — scripted surface check against the local reader

Purpose: run the repository diagnostic end-to-end. The script speaks HTTP base
URLs; against a UDS you lend it `--unix-socket` through its documented
`FRAMENEST_CURL_BIN` hook (no repository change needed).

```fish
# [MacBook / fish]
printf '%s\n' '#!/usr/bin/env bash' \
  'exec curl --unix-socket "$FRAMENEST_UDS_PATH" "$@"' > $ACC/curl-uds.sh
chmod +x $ACC/curl-uds.sh
env FRAMENEST_PUBLIC_BASE_URL=http://localhost \
    FRAMENEST_CURL_BIN=$ACC/curl-uds.sh \
    bash scripts/operator/infosec/framenest_public_surface_check.sh
#------------------------------------------------------
```

Expected output class (paste the whole table back to the Orchestrator):

```text
PROBE                                          HTTP   HEADERS   BODY      RESULT
GET /infosec-surface-probe-unlisted (reference) 404    ok        ok        PASS
GET /docs                                      404    ok        ok        PASS
GET /redoc                                     404    ok        ok        PASS
GET /openapi.json                              404    ok        ok        PASS
GET /api/admin/analysis-proposals              404    ok        ok        PASS
POST /api/media (denied route)                 404    ok        ok        PASS
GET /api/media/not-a-uuid                      404    ok        ok        PASS
RESULT: PASS — uniform sanitized 404 posture verified.
```

Failure: any row FAIL — include the table verbatim; the failing dimension
(HTTP / HEADERS MISSING / BODY DIFFERS) names the broken contract.
Report: cite **A7**.

### A8 — manual uniform-404 spot checks

Purpose: eyeball the byte-level contract yourself, including a malformed UUID
and out-of-range pagination (`d3b203f`, F-1).

```fish
# [MacBook / fish]
for p in "/docs" "/api/media/not-a-uuid" "/api/media?limit=9999" "/api/admin/media"
    curl -s --unix-socket $ACC/sockets/public.sock "http://localhost$p"; echo
end
#------------------------------------------------------
```

Expected: four identical bodies,
`{"error":{"code":"NOT_FOUND","message":"Not found."}}`, all status 404
(verify one with `-o /dev/null -w "%{http_code}\n"`).
Failure: any divergent body/status. Report: cite **A8**.

### A9 — socket permission gate (positive control)

Purpose: see the third diagnostic pass on sockets you just created, then fail
on a deliberately bad fixture.

```fish
# [MacBook / fish]
touch $ACC/sockets/bad.sock; chmod 604 $ACC/sockets/bad.sock
env FRAMENEST_SOCKET_PATHS="$ACC/sockets/public.sock:$ACC/sockets/bad.sock" \
    bash scripts/operator/infosec/framenest_socket_permissions_check.sh
#------------------------------------------------------
```

Expected: `public.sock` row PASS (type `socket`, no world bits); `bad.sock`
row FAIL (`not-a-socket`/world-access); overall rc=1.
Failure: unexpected column values — paste the table. Report: cite **A9**.

### A10 — clean shutdown

```fish
# [MacBook / fish]
./framenest stop
rm -rf $ACC
#------------------------------------------------------
```

Expected: launcher stops its server; acceptance directory removed. (Stop the
public-reader terminal with Ctrl-D/Ctrl-C first.) Report: cite **A10** only if
something fails.

---

## Part B — NUC / Tailscale verification (CONDITIONAL — read the banner)

> **Honesty banner:** your production NUC still serves the older accepted
> release (`aec2f009…`, schema `0028`, per `README.md` Status and
> `SECURITY.md`). Everything this whole shipped reaches the NUC **only after a
> separately authorized immutable release update** through
> `deploy/ubuntu/framenest-release`. If you have not deployed a release
> containing `be35922`, skip Part B entirely — there is nothing there to test
> yet, and attempting these flows against the old release proves nothing about
> this whole.

If, and only if, a later authorized deployment ships this whole:

- **B1 — ordinary mapped user flows over Tailscale Serve** (requires your live
  identity mapping and real data — privacy reminder: use your own test items,
  never private media): sign in through your tailnet origin; verify own-gallery
  workspace list shows only your contributions (`5b99575` semantics),
  submit one analysis proposal (expect 201, second within the hour eventually
  429 after six), manage your own alias; confirm you cannot see another user's
  proposals or aliases.
- **B2 — administrator review inbox**: confirm the companion review inbox and
  Apply behave exactly as before (`be35922` touched none of it); publish one
  reviewed item via the administrator route only.
- **B3 — companion extension regression**: Save/Apply from the side panel on
  an X page; expect unchanged behavior and unchanged extension-origin rules
  (`SECURITY.md`, companion paragraphs).
- **B4 — log triage on the NUC** (read-only; counts only):

```text
# [NUC / bash]
env FRAMENEST_LOG_UNIT=framenest.service FRAMENEST_LOG_SINCE="-24h" \
    bash scripts/operator/infosec/framenest_log_triage.sh
#------------------------------------------------------
```

  Expected: counts print; RESULT CLEAN unless something abnormal happened.
  Privacy: never paste raw journal lines into chat — the tool prints counts
  precisely so you do not have to.

Every B step: purpose = regression of shipped behavior under real identity;
failure reporting identical (step id + captured output). Marked clearly:
B1–B3 require live identity mapping and production data; B4 requires journal
read membership.

---

## Part C — explicitly NOT testable yet

These remain impossible to verify anywhere until their own wholes exist —
do not attempt them, and treat any apparent success as misconfiguration:

- Public TLS bind of the reader, HSTS/ACME baseline — preflight whole;
  checklist: `docs/INFOSEC.md` §4.3.
- Proxy-owned rate limits, connection caps, timeouts (audit F-8/C3) —
  `docs/INFOSEC.md` §4.4.
- VPS hosting of the public origin — ranked option 4 in ADR-0074, needs its
  own operational decision; `docs/INFOSEC.md` §1.
- Reader/writer atomic release ordering (F-7 rule) — exercised only by the
  first post-migration release; `docs/INFOSEC.md` §4.10.

---

## Report-back template

Copy, fill, and send back (screenshots optional; raw journals/secrets never):

```text
Acceptance run — framenest-public-published-surface-and-tailscale-workspace
Tested at HEAD: be35922d223c49f3b140453e69b313c9086c3831
Part A: A0 [PASS/FAIL] … A10 [PASS/FAIL]   (A7 table pasted above/below)
Part B: SKIPPED (release not deployed) | B1..B4 results
Part C: acknowledged as deferred
Deviations / notes: <free text>
Failed step ids + evidence: <e.g. A7 — BODY DIFFERS on /openapi.json, table attached>
```

A single-line reply "Part A all PASS, Part B skipped" is a complete positive
result.

---

## Terminal outcome

```text
Terminal outcome: PASS
Escalation disposition: none
Logical-whole closure: not claimed (Orchestrator-owned)
```

Guide authored within the single allowlisted Meta write (corrected
`framenest` path); zero repository mutations (worktree clean before and after
writing); every printed command verified against launcher docs, pyproject
entry points, and the scripts' own headers/live usage runs at HEAD
`be35922d223c49f3b140453e69b313c9086c3831`. Two non-blocking script polish
items (executable bit, `-h` early exit) routed to the Orchestrator above.
Authority expires with this report.
