### Report for ORCHESTRATOR_CHAT

Logical whole identity: youtube-fixes
Worker session ordinal: 03
Worker exchange ordinal: 01
Persistent role identity: WORKER
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Independent Audit
Phase: acceptance
Task identity: ACCEPT-YOUTUBE-INSPECTION-PROJECTION-01
status: PASS
Phase-qualified result: acceptance-PASS
Start commit: eb5af0e49729eaf87eb3210ce0fd87295daae826
End commit: eb5af0e49729eaf87eb3210ce0fd87295daae826
Report justification: final-acceptance
Logical-whole closure: not-closed

Independence holds. This session did not plan, implement, correct, or materially participate in candidate `eb5af0e49729eaf87eb3210ce0fd87295daae826`. Its first input is the acceptance prompt. The candidate was inspected from that prompt, the named artifacts, the repository at the candidate commit, and the installed package source.

## Acceptance and Correction Record

```text
Acceptance candidate: eb5af0e49729eaf87eb3210ce0fd87295daae826
Acceptance owner map: approved plan 01_report_00.md; implementation prompt 02_implementation_00.md; implementation report 02_report_00.md; candidate diff 2c4f4d8..eb5af0e; four changed paths; SPEC.md sentence; installed yt-dlp 2026.7.4 source
Acceptance allowlist: src/kronika/infrastructure/youtube/downloader.py; tests/unit/infrastructure/youtube/test_downloader.py; tests/integration/test_youtube_acquisition_lifecycle.py; SPEC.md
Acceptance risk claims: projection preserves the consumed metadata and format-selection fields; bounded inspection output remains bounded with correct early termination; download behavior is unchanged; failure stage/code and companion status are unchanged; no pin, schema, extension, API, CLI or companion change; no secret or private payload leakage; the two binding corrections are applied
Acceptance control matrix: C01-C29
Acceptance independence: required-fresh-independent
Primary fresh acceptances used: 1
Automatic corrections used: 0
Correction re-acceptance: not-applicable
Named missing-evidence probe: none
Out-of-scope observations: none
```

## Candidate identity

Candidate commit: `eb5af0e49729eaf87eb3210ce0fd87295daae826`
Parent commit: `2c4f4d89375628df28926060aba305e5d80bacff`
Subject: `fix: project youtube inspection metadata`
Branch: `main`, one commit ahead of `origin/main` and zero behind; `origin/main` is the parent. Decoration is `HEAD -> main` with no tag.
Local-only: yes. This acceptance did not push, tag, fetch, or change a branch or remote.
Worktree: clean before and after the focused test.
Governing AP: `.ap` `HEAD` and the `HEAD` gitlink are both `d7023cf037f6d17885c3ede5c04812c61640da50`. The candidate diff does not change the submodule.

Exact changed paths:

- `src/kronika/infrastructure/youtube/downloader.py`
- `tests/unit/infrastructure/youtube/test_downloader.py`
- `tests/integration/test_youtube_acquisition_lifecycle.py`
- `SPEC.md`

## Changed files and purpose

This acceptance wrote only this report. The repository candidate was not mutated. The report records the independent acceptance of the local candidate above.

## Control matrix

### C01 PASS

`git status --porcelain=v1 -b` is `## main...origin/main [ahead 1]` with no path lines. `git rev-parse HEAD` is `eb5af0e49729eaf87eb3210ce0fd87295daae826`. `git rev-parse HEAD^` and `git rev-parse origin/main` are both `2c4f4d89375628df28926060aba305e5d80bacff`. `git rev-list --count` is 1 ahead and 0 behind. `git -C .ap rev-parse HEAD` and `git ls-tree HEAD .ap` are both gitlink `d7023cf037f6d17885c3ede5c04812c61640da50`.

### C02 PASS

`git diff-tree --no-commit-id --name-status -r HEAD` is exactly four modifications: `SPEC.md`, `src/kronika/infrastructure/youtube/downloader.py`, `tests/integration/test_youtube_acquisition_lifecycle.py`, and `tests/unit/infrastructure/youtube/test_downloader.py`. `git status --porcelain=v1` has no untracked path. `git diff --submodule=short 2c4f4d8..eb5af0e -- .ap` is empty. `git diff --check 2c4f4d89375628df28926060aba305e5d80bacff..eb5af0e49729eaf87eb3210ce0fd87295daae826` exits 0 with no output. The same check was repeated after the focused test and remained clean.

### C03 PASS

`git log -1` subject is exactly `fix: project youtube inspection metadata`. The parent is the current `origin/main`. The commit decoration is `HEAD -> main` and carries no tag. The diff contains no deployment, release, or remote-configuration path. This acceptance performed no push, tag, branch, remote, NUC, or deployment action.

### C04 PASS

`inspect` builds `sys.executable -I -m yt_dlp`, then the existing common flags, then `--simulate`, `--no-write-info-json`, `--print` with `INSPECTION_METADATA_TEMPLATE`, `--print` with `INSPECTION_FORMATS_TEMPLATE`, `--`, and `identity.canonical_url` (`downloader.py` lines 183-192). `--dump-single-json` and `--skip-download` are absent from that tuple. The common flags contain no cookie argument. `test_attestation_and_inspection_use_exact_isolated_argv_and_environment` pins that argv, both template strings, the absence of `--dump-single-json` and `--skip-download`, and the absence of any argument containing `cookie`. It also pins `start_new_session` and the five-variable environment without `HOME` or `HTTP_PROXY`.

### C05 PASS

The metadata template is exactly `%(.{extractor_key,id,_type,is_live,live_status,availability,age_limit,duration,title,channel,channel_id,upload_date,_filename,filename})j`. Those are the fields `_inspection_from_payload` reads, apart from `formats`, which comes from line 2. The formats template is exactly `%(formats.:.{format_id,ext,video_ext,audio_ext,vcodec,acodec,height,width,fps,tbr,abr,asr,filesize,filesize_approx,has_drm})j`. `_select_plan`, `_format_size`, `_format_quality_key`, and `_audio_quality_key` read only those format fields. Neither template contains a URL, fragment, caption, thumbnail, heatmap, chapter, comment, or description field. The equivalence test asserts that the projected text omits `description`, `thumbnails`, `automatic_captions`, `subtitles`, `heatmap`, `fragments`, and `"url"`.

### C06 PASS

`_projected_inspection_document` decodes UTF-8 strictly, drops only trailing empty lines, and requires exactly two non-empty lines (`downloader.py` lines 817-825). Line 1 must be one JSON object and must not contain `formats`. Line 2 must be the literal `NA` or one JSON list. The function does not log either line, and `downloader.py` contains no logger or print call. Successful inspections, including the argv test and the equivalence test, use a projection that ends in a newline; those passes show that the trailing empty line is ignored. A raw line is not present in the exception text asserted by the malformed-projection test.

### C07 PASS

`test_at_cap_two_line_inspection_keeps_the_existing_plan` builds a valid two-line projection of length `INSPECTION_STDOUT_LIMIT_BYTES` (`1_048_576`) and stderr of length `INSPECTION_STDERR_LIMIT_BYTES` (`65_536`). The inspection returns the existing plan `137+140` with expected size 120, and the recorded signal list stays empty. Exact-cap capture is not overflow: `_capture_stream` sets the overflow flag only when a chunk is longer than the remaining room.

### C08 PASS

`test_inspection_overflow_is_output_limit` case `(stdout_over=1, stderr_over=0, returncode=0)` feeds stdout of `1_048_576 + 1` bytes. `inspect` checks `stdout_overflow` or `stderr_overflow` before `returncode` and before `_projected_inspection_document` (`downloader.py` lines 204-212). The result is `INSPECTION_OUTPUT_LIMIT`. The same bytes are not valid projection JSON, so a parse-first order would have produced `INSPECTION_INVALID_OUTPUT`.

### C09 PASS

The same parametrized test case `(0, 1, 0)` keeps a valid under-cap projection on stdout and sets stderr to `65_536 + 1` bytes. The result is `INSPECTION_OUTPUT_LIMIT`.

### C10 PASS

The same parametrized test case `(1, 1, 0)` puts both streams one byte over their caps. The result is `INSPECTION_OUTPUT_LIMIT`.

### C11 PASS

`test_far_over_inspection_retains_the_cap_and_kills_the_group` supplies `1_048_576 + 100_000` stdout bytes through a process that does not exit until `SIGKILL`. The fake stream returns its whole buffer on the first `read`. With `stop_after_limit=True`, `_capture_stream` retains `chunk[:remaining]` and breaks on that overflowing chunk (`downloader.py` lines 781-787). The test records retained stdout `(1_048_576, True)`, `process.stdout.reads == 1`, and signals `[SIGTERM, SIGKILL]`. The result is `INSPECTION_OUTPUT_LIMIT`. `_stop_for_overflow` calls the existing `_terminate_process_group` helper, which sends `SIGTERM` and then `SIGKILL`.

### C12 PASS

The parametrized case `(1, 0, 1)` combines stdout one byte over the cap with return code 1. Overflow is tested before the return code, so the result is `INSPECTION_OUTPUT_LIMIT`.

### C13 PASS

`test_inspection_nonzero_exit_without_overflow_fails` uses a valid under-cap projection and return code 1. The result is `INSPECTION_FAILED`, and the recorded signal list stays empty.

### C14 PASS

`test_hanging_inspection_times_out` uses a child that waits until `SIGKILL`, with the inspection timeout at 0.05 seconds. `_run_bounded` raises `YouTubeDownloadError("SUBPROCESS_TIMEOUT")` after the existing TERM/KILL helper, and `inspect` maps that error to `INSPECTION_TIMEOUT`. The test records `[SIGTERM, SIGKILL]`.

### C15 PASS

`test_malformed_projection_is_invalid_output` covers every listed shape, and each result is `INSPECTION_INVALID_OUTPUT`:

- partial JSON: `{"extractor_key":"Youtube"` followed by a formats line
- invalid JSON: `not-json` followed by a formats line
- empty stdout
- one full JSON object, `json.dumps` of the inspection payload
- metadata-line `NA` followed by `[]`
- a non-UTF-8 byte `\xff` followed by a formats line
- a JSON list on line 1
- a metadata object whose line contains `formats`
- a JSON object on line 2

The parser implements those rejects at `downloader.py` lines 817-843. The metadata-line `NA` result is `INSPECTION_INVALID_OUTPUT`, which is binding correction 2.

### C16 PASS

`test_formats_line_na_selects_no_visual_stream` sends a valid metadata line and the literal formats line `NA`. `_projected_inspection_document` turns that `NA` into `[]` (`downloader.py` lines 835-836). `_inspection_from_payload` then calls `_select_plan([])`, which raises `NO_VISUAL_STREAM` because there is no visual or combined stream (`downloader.py` lines 388-389). The test result is `NO_VISUAL_STREAM`.

### C17 PASS

`_run_download` still captures with `MAX_STDOUT_BYTES` and `MAX_STDERR_BYTES` and does not pass `stop_after_limit` or `terminate_on_overflow` (`downloader.py` lines 445-449). Those names and values remain `1_048_576` and `65_536` (`downloader.py` lines 55-56). The download diff does not change download argv, the return-code check, or the overflow check after process exit. `test_download_output_limit_waits_for_exit_without_kill` covers stdout overflow and stderr overflow. Each raises `DOWNLOAD_OUTPUT_LIMIT`, records no `killpg` signal, and reads the overflowing stream twice: one full read and the following empty read, which is EOF for this fake. `_capture_stream` with `stop_after_limit=False` continues after the overflow flag until the empty chunk.

### C18 PASS

`test_projected_formats_match_full_payload_selection` mode `split` compares `_inspection_from_payload` on the full info dict with `inspect` on the two-line projection. Both produce `YouTubeDownloadPlan` video `137`, audio `141`, expected size `1040`, `has_source_audio=True`, `split_streams=True`. The full dict also contains a higher-height later stream, a DRM stream, an over-cap pair, format URLs, fragments, captions, a heatmap, a description, and thumbnails. Those extra keys are absent from the projected stdout. Advisory title, channel, channel id, source date `2026-07-01`, and remote filename match.

### C19 PASS

Mode `combined` makes every split pair exceed the final-size cap. Both the full payload and the projection select video `22`, no audio, expected size `800`, `has_source_audio=True`, `split_streams=False`.

### C20 PASS

Mode `silent` has no audio stream. Both paths select video `137`, no audio, expected size `1000`, `has_source_audio=False`, `split_streams=False`.

### C21 PASS

The over-cap code is `COMPATIBLE_FORMAT_UNAVAILABLE`. Mode `over-cap` expects that code from both `_inspection_from_payload` on the full payload and `inspect` on the projection, and the focused run passed. `_select_plan` returns a plan only when the expected size is missing or within `max_final_size_bytes`; when the source has audio and every sized split pair and combined stream is over that cap, it raises `COMPATIBLE_FORMAT_UNAVAILABLE` at `downloader.py` line 419. The later `FINAL_SIZE_LIMIT` check in `_inspection_from_payload` (lines 316-320) runs only after a plan has already been returned. The candidate diff does not change `_select_plan` or `_inspection_from_payload`. Classification: the plan's historical name `FINAL_SIZE_LIMIT` for this case. The candidate preserves the existing selector.

### C22 PASS

The candidate diff does not include `src/kronika/application/youtube_acquisition.py`, `src/kronika/adapters/api/youtube_request_api.py`, `src/kronika/adapters/cli/youtube.py`, or any `extension/` path. `YouTubeAcquisitionCoordinator._process` still maps `YouTubeInspectionError` to stage `YouTubeFailureStage.INSPECTION`, whose value is `inspection` (`youtube_acquisition.py` lines 1109-1114; `YouTubeFailureStage.INSPECTION = "inspection"`). The request snapshot still sets `failure_category` from that stage value and copies `failure_code` (`youtube_acquisition.py` lines 788-791). `YouTubeRequestItemResponse` still exposes both fields (`youtube_request_api.py` lines 80-81) and `_item` copies them. Operator `_write_status` still prints `failure_stage` and `failure_code` (`youtube.py` lines 425-437). `status` without `--wait` uses `fail_on_failed=False` and returns 0 (lines 274-276 and 402-422). `ingest` and `status --wait` use `_wait_for_terminal` with `fail_on_failed=True`; `main` maps `_TerminalFailureError` message `YouTube acquisition failed.` to exit 4 (lines 190-196). `youtubeSnapshot()` copies `failureCategory` and does not copy `failure_code`; phase `failed` becomes outcome `failed` (`service_worker.js` lines 252-263). Companion history maps that phase through `YOUTUBE_DOWNLOAD_STATUS_BY_PHASE.failed` to `DOWNLOAD_STATUS_TEXT.failed`, which is `Download failed` (`messages.js` lines 92 and 107-114). The integration test `test_inspection_output_limit_fails_claim_and_skips_download` reaches the existing coordinator path: state `FAILED`, stage `inspection`, code `INSPECTION_OUTPUT_LIMIT`, cleanup `complete`, staging removed, and `download_calls` empty.

### C23 PASS

`SPEC.md` lines 781-785 add the sentence: inspection requests only the metadata and format-selection fields the server consumes, retains at most 1 MiB of inspection standard output and 64 KiB of inspection standard error, terminates that inspection subprocess when either cap is exceeded, and a larger document fails closed as `INSPECTION_OUTPUT_LIMIT` without being parsed or logged. That matches the candidate constants `1_048_576` and `65_536`, the early termination, and the no-parse overflow path. The sentence does not claim a larger cap, a pin change, a parser detail, or a companion change. The candidate diff does not change an ADR, `README.md`, or `docs/X_COMPANION.md`.

### C24 PASS

The owners comment at `downloader.py` lines 59-62 cites `yt_dlp-2026.7.4.dist-info/METADATA`, `yt_dlp/options.py`, and `yt_dlp/YoutubeDL.py` for `prepare_outtmpl`, `traverse_obj`, `_forceprint`, and the `dump_single_json` wrapper. The candidate does not cite `README.txt`. The installed tree has no `yt_dlp-2026.7.4.dist-info/README.txt`. Installed evidence: `METADATA` `Version: 2026.7.4`, the OUTPUT TEMPLATE section, and the `--print` text; `options.py` lines 1260-1266 register repeatable `--print` with `when_prefix` append; `YoutubeDL.py` defines `prepare_outtmpl` at line 1269, calls `traverse_obj` from it at line 1347, defines `_forceprint` at line 3220, returns on `simulate` before description and subtitle writes at lines 3376-3379, and wraps `dump_single_json` at lines 3699-3701. The helper docstring also names `outtmpl_na_placeholder` against METADATA. METADATA's user-facing flag is `--output-na-placeholder` with default `NA` (METADATA lines 746-747 and 1538); the Python parameter `outtmpl_na_placeholder` is in `YoutubeDL.py` line 1388. The required owners citation remains accurate. This name pairing has no runtime effect and does not fail C24.

### C25 PASS

`git diff-tree` is only the four allowlisted paths. `pyproject.toml` still pins `yt-dlp==2026.7.4` and is outside the commit. The diff contains no schema, migration, extension, API, CLI, companion, X-acquisition, permission, route, provider, or dependency change. R-2 and R-3 from the predecessor closure remain untouched. No household onboarding, error-copy, accessibility, modularization, or product-language work is in the diff.

### C26 PASS

`downloader.py` has no logger and no print. Overflow handling stores at most the cap and does not log the retained bytes. The new tests use the existing synthetic video id, the titles `Synthetic title` and `Synthetic channel`, the filename `Remote title.mp4`, and `https://example.invalid/` URLs. The malformed-projection test asserts that the video id is absent from the exception string. The argv test asserts that no cookie argument is present and that `shell` is absent from the subprocess kwargs. `_spawn` remains `create_subprocess_exec` through the process factory, with `stdin` devnull and `start_new_session=True`. This acceptance made no live network call and did not read a secret, credential, cookie, or browser profile.

### C27 PASS

```text
./.ap/ap exec --root /Users/agile/Projects/kronika --baseline 2c4f4d89375628df28926060aba305e5d80bacff --operation test-focus -- tests/unit/infrastructure/youtube/test_downloader.py tests/integration/test_youtube_acquisition_lifecycle.py -q -p no:cacheprovider
```

Result: `48 passed in 4.55s`, 0 failed. The candidate-mode check `./.ap/ap project check --root /Users/agile/Projects/kronika --candidate` reported `PASS (non-authorizing)` and is readiness evidence only. `git diff --check` on `2c4f4d8..eb5af0e` is clean. After the test, `git status --porcelain=v1 -b` is still `## main...origin/main [ahead 1]` with no untracked path. The four candidate paths remain the only commit changes.

### C28 PASS

A formats line whose text is JSON `null` takes the non-`NA` branch. `json.loads("null")` is `None`, `None` is not a list, and `_projected_inspection_document` raises `INSPECTION_INVALID_OUTPUT` (`downloader.py` lines 835-843). Classification: accepted residual of the approved parser spec. Line 2 must be one JSON list or the literal `NA`. JSON `null` is neither. It does not replace the approved no-formats outcome. Installed `prepare_outtmpl` replaces a `None` value with the default placeholder `NA` before the `j` conversion (`YoutubeDL.py` lines 1468-1476), so the tool's missing or null formats value is the literal `NA`. Binding correction 2 maps that `NA` to `[]` and `_select_plan([])` raises `NO_VISUAL_STREAM`, which is the result asserted by C16. No repair was made.

### C29 PASS

This acceptance used read-only Git inspection, file reads, and the two declared AP commands: candidate-mode project check and the focused `ap exec` test. No NUC, SSH, sudo, deployment, publication, live YouTube, live `yt-dlp`, provider, browser, or external-service action occurred. No repository or host mutation occurred.

## Tests and validation

Focused test count: 48 passed, 0 failed. `git diff --check`: clean, exit 0. Candidate identity evidence is C01-C03. Candidate-mode project check: PASS, non-authorizing.

C21 over-cap code: `COMPATIBLE_FORMAT_UNAVAILABLE` on both the full payload and the projection. This is the plan's historical naming of `FINAL_SIZE_LIMIT`; the unchanged selector raises `COMPATIBLE_FORMAT_UNAVAILABLE` when the source has audio and every sized candidate is over the cap.

C28 formats-line JSON `null` code: `INSPECTION_INVALID_OUTPUT`. Classification: accepted residual of the approved parser spec.

## Commit and push result

None. Acceptance did not create a commit and did not push. Start and end commit remain `eb5af0e49729eaf87eb3210ce0fd87295daae826`.

## Deviations, risks, and missing evidence

No control failed. The docstring beside the parser names METADATA `outtmpl_na_placeholder`; the installed long description calls the same default `NA` placeholder `--output-na-placeholder`, and `YoutubeDL.py` holds the parameter name. The required owners comment is accurate, and runtime behavior is unchanged.

The two binding corrections are present: the citation does not use `README.txt`, and formats-line `NA` preserves `NO_VISUAL_STREAM` while metadata-line `NA` stays `INSPECTION_INVALID_OUTPUT`.

No required artifact, test, plan section, ADR, or installed-package source was missing. Publication, NUC deployment, the live attempt on the private video, rendered acceptance, and logical-whole closure were not part of this grant and remain separate.

No repository, host, NUC, network, publication, or deployment mutation occurred.

## Next step

The Orchestrator decides acceptance disposition for local commit `eb5af0e49729eaf87eb3210ce0fd87295daae826`. Publication, NUC deployment, the live attempt on the private video, and rendered acceptance each require a separate Cooperator grant.

## Authority expiry

This terminal report ends the acceptance grant. No autonomous continuation is authorized. Only the Orchestrator may decide acceptance disposition and closure after reconciling this report.

```text
Orchestration critique:
MEASURED: none
LEAD: none
```

Resolved Execution Issues / Near-Misses: none
Pre-Existing Failure Classification: none
Logical-whole closure: not-closed
