### Report for ORCHESTRATOR_CHAT

Logical whole identity: bookradar-review-and-promotion-workflow
Worker session ordinal: 01
Worker exchange ordinal: 02
Persistent role identity: WORKER
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BOOKRADAR-REVIEW-PROMOTION-IMPLEMENT
status: PASS
Phase-qualified result: implementation-PASS
Start commit: 2281982f7dae0ef1f582d294592c41281ba11b21
End commit: 69ec45e245108c90e2de4302c03ca72572bf1829
Changed files: README.md (synthetic show/promote/review workflow and UI offer flags); crates/bookradar-store/src/lib.rs (export candidate and promotion); crates/bookradar-store/src/research.rs (read-only CandidateQuery and candidate); crates/bookradar-store/src/promotion.rs (new; promote and append_application_review); crates/bookradar-store/src/bin/bookradar-review.rs (new; show, promote, review); crates/bookradar-store/tests/promotion.rs (new; 12 library tests); crates/bookradar-store/tests/review_cli.rs (new; 4 process tests); crates/bookradar-ui/src/config.rs (optional --source-id and --offer-id, default 1 and 1); crates/bookradar-ui/src/snapshot.rs (load the configured offer); crates/bookradar-ui/src/render.rs (print the configured offer); crates/bookradar-ui/tests/cli.rs (invalid ids exit 2 before I/O); crates/bookradar-ui/tests/render.rs (non-default offer and promoted checked-available); crates/bookradar-ui/tests/common/mod.rs (config_at sets source 1 and offer 1); docs/adr/0008-governed-review-and-promotion.md (new; Accepted 2026-11-14, nine cells, positive-only scope)
Tests and validation: `bash scripts/verify.sh` exit 0 on the clean commit. The gate ran `cargo +1.99.1 test --workspace --locked --offline` and reported 113 tests: verification 17, store lib 10, poc/research/review bins 0, store cli 4, history 13, persistence 6, promotion 12, research_cli 2, research_contract 5, research_ingestion 20, review_cli 4, ui lib/main 0, ui cli 4, http 6, render 10, doc-tests 0. The 19 new tests are promotion 12, review_cli 4, render 2, ui cli 1. `cargo +1.99.1 fmt --all --check` and `clippy --workspace --all-targets --locked --offline -- -D warnings` passed inside the gate. Core tree is one line: `bookradar-core v0.1.0 (/Users/agile/Projects/bookradar)`. `git diff --check` passed. Strict `./.ap/ap doctor` PASS, variant stable, pin `d7023cf037f6d17885c3ede5c04812c61640da50`. `git status --porcelain` empty after the gate. Playwright and the browser were not run.
Git result: one local commit on main (69ec45e245108c90e2de4302c03ca72572bf1829, parent 2281982f7dae0ef1f582d294592c41281ba11b21, tree fcbc929b25015952478d5d9f0eb2719bedb820c9); subject `feat: add a governed research review and promotion path`; no push
Deviations, risks, or missing evidence: `--position 0` is valid and receipt `0` is usage. A planning sentence that every id rejects 0 would have made the `newer.json` demonstration impossible; the schema and the approved fixtures control. A structurally rejected row with a NULL finding id is `unknown-finding`, which the plan allowed beside `not-admitted`. `promote` takes a store path and opens the store only after the candidate and attestation pass, so a refusal does not create the file. The replayed-row assertion uses receipt 3 position 0: partial.json is receipt 1, `newer.json` is receipt 2 and stays admitted, and the envelope with `reported_run_outcome` changed from `succeeded` to `failed` is receipt 3 and `replayed`. No rendered browser evidence. This report does not certify acceptance, publication, or closure.
Smallest next step: Fresh Independent Audit (02/01) on candidate 69ec45e245108c90e2de4302c03ca72572bf1829
Report justification: new-mutation
Logical-whole closure: not-closed
Authority expiry: this terminal report ends the implementation grant; no autonomous continuation.
Prompt SHA-256: `04747fbabb2d9d7973943b7be3a419fdb54af735d4eda60eb73cf86dc3957926`
Orchestration critique:
MEASURED: the focused pre-commit inventory listed 113 tests, and `bash scripts/verify.sh` then exited 0 on the same clean commit.
LEAD: none
Resolved Execution Issues / Near-Misses: the first `show` allowlist rejected `--finding` because it was empty; `CARGO_BIN_EXE_bookradar-review` must keep the hyphen, matching the existing binaries; promotion tests called a store helper name that does not exist and initially pointed the replayed row at receipt 2; clippy rejected needless borrows in the CLI test. Cause: the first drafts did not match the parser, Cargo's binary env name, or `common::create`. Resolution: all four were corrected inside the allowlist before the single commit. Residual risk: none in the committed tree; the gate passed.
Pre-Existing Failure Classification: none

## Implementation summary

`bookradar-review` adds `show`, `promote`, and `review` in `bookradar-store`. `bookradar-poc` and `bookradar-research` are unchanged. `show` opens the research ledger read-only. `promote` writes one application-store observation only for an `admitted` finding with a complete positive reviewer attestation: resolved edition, Slovak, readable, present, available, all three claims covered, `direct-browser` or `manual` evidence, and reviewer approval. Agent-only evidence is refused before the store file is created. Stale positive rows may be stored and stay not eligible. There is no negative or unavailable promotion path. Provenance is `research:<producer>/<run>/<finding>@<receipt>/<position>`. Fact fields come from the reviewer flags. Human reviews stay in application id `0x42524452`. The ledger has no `append_review`. Caller-supplied source, offer, and observation ids collide as `duplicate-key` with no partial write. The same finding may be cited again under a new observation id. An admitted finding may be promoted while ledger knowledge is `disputed`, and `show` prints that dispute. Policy refusals exit 1 with `unknown-finding`, `not-admitted`, `agent-only-evidence`, or `incomplete-attestation`. Exit 2 is usage before I/O. There is no exit 4.

`bookradar-ui` accepts optional `--source-id` and `--offer-id`, both defaulting to 1. Invalid ids exit 2 before I/O. The page prints the configured offer. A promoted source-1 offer-1 observation renders `Checked available` through the existing kernel. The matching research candidate stays unreviewed and not eligible. ADR 0008 records the nine approved cells, status Accepted 2026-11-14, date 2026-11-14, decision owner COOPERATOR. The domain contract, research input contract, schemas, core, lockfile, and ADRs 0001–0007 were not edited.
