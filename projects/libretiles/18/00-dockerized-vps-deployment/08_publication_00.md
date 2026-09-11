# Worker Prompt: Publish Accepted Dockerized VPS Candidate

You are one fresh Worker instance assigned to the persistent WORKER role. This is a complete fresh-session publication grant for the accepted candidate of logical whole `dockerized-vps-deployment`. Publication is a separate surface: you may perform only the exact Git operations below and must not modify file content.

Logical whole identity: dockerized-vps-deployment
Worker session ordinal: 08
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker (publication)
Phase: Publication
Task identity: DVP-PUBLISH-01
Reasoning recommendation: medium, because the operation is a bounded conventional commit and non-force push with direct public readback; it must stage exactly the accepted candidate and change nothing else.

## Delivery

Prompt source: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/08_publication_00.md`
Write the terminal report atomically to: `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/08_report_00.md`

Do not overwrite prior Meta artifacts. After writing the report, return only its exact path and stop.

## Repository Identity And Publication Gate

Working directory: `/home/agile/Projects/libretiles`
Repository checkout topology: standalone checkout
Repository identity: `https://github.com/cisarik/libretiles`
Expected branch: `main`
Expected parent commit / current HEAD and `origin/main`: `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`
Expected AP gitlink and `.ap` HEAD: `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`
Expected index: clean
Expected candidate inventory digest: `c2d08f489e2bc038899d7633651b856e593d880d8c067cae0a67c019a97437a9` under the established ordered NUL-delimited `git status --porcelain=v1 --untracked-files=all` record plus present-content SHA-256 or `DELETED` marker method
Expected accepted state: Meta `07_report_00.md` `acceptance-PASS`, candidate `c2d08f48...`

Before mutation, verify repository root/Git directory, remote URL, branch, HEAD, `origin/main`, AP equality, clean index, complete 45-path candidate inventory, digest equality, absence of active Git operations/locks, intended commit identity, and that the `main` push is non-force. Stop without mutation on any mismatch or if any status path is outside the accepted 45-path candidate.

## Accepted Publication Decision

The Cooperator authorized commit plus non-force push of the accepted candidate. Publication is not deployment: no host, container runtime, registry, or production system is touched by this exchange.

## Command Authority

Authorized Git writes, in exact order:

1. Re-verify the 45-path status set and digest.
2. Stage exactly the verified candidate path set. `git add -A` is authorized only after the set is proven equal to the accepted candidate and contains no path outside it.
3. Create one commit with this exact message:

```text
feat(deploy): add hardened Docker Compose production deployment

Replace the systemd/host-nginx production path with a single Docker Compose
topology: nginx as the only public edge, loopback-bound Next standalone in
nginx's network namespace, Daphne on a group-restricted Unix socket, a
dedicated secret-reader group, Certbot TLS lifecycle, and verified
PostgreSQL backup/restore. Supersede the host deployment templates and add
static and disposable-Docker validation guards.
```

4. Verify the commit: parent equals `f6ec9bf50e48c5b8ca97b840b019752e82b58cd6`; commit contains exactly the accepted 45 paths; working tree and index clean afterward; no path outside the candidate; no secret-like value added.
5. Push non-force to `origin main`: `git push origin main`.
6. Direct public readback: confirm `git ls-remote origin refs/heads/main` reports the new commit, and confirm the public ref is not ahead of or behind the local commit.

Negative authority: no file content change; no amend, rebase, force-push, tag, branch creation, merge, cherry-pick, revert, reset, restore, checkout, stash, clean, remote/config change, or submodule update; no GitHub settings, releases, actions, or PRs; no registry or image publication; no deployment or production action; no other repository path; no Meta mutation other than the exact report path; no real secret, dotenv, account, or user data.

Dependency authority: none.
Network authority: the exact GitHub remote endpoints required for `git push` and `git ls-remote` only. No provider, catalog, registry, ACME, DNS, browser, or other endpoint.
Secret authority: none; never print credentials, tokens, or remote URLs containing credentials.
Git authority: exactly the stage/commit/push/readback sequence above; all other Git writes remain prohibited.
Side-effect authority: one local commit, one non-force remote branch update on `origin/main`, and the exact report write.
Internal delegation posture: not-used
Accountable Worker: one WORKER

## Validation

- `git diff --check` clean before staging.
- Post-commit `git status --porcelain=v1` empty; `git rev-parse HEAD^` equals the expected parent; `git show --name-status --format=` lists exactly the accepted 45 paths.
- Public readback via `git ls-remote` equals the new local HEAD.
- Report the exact commit SHA, tree/path count, push result, and readback result.
- If the push fails or the remote has advanced, stop and report `BLOCKED` with the exact error; do not force, rebase, or rewrite anything.

Evidence tier: E2 (bounded publishable commit and non-force branch update with direct readback)
Security task class: publication of an acceptance-PASS candidate
Security route: publication surface only; R4/R6 evidence already recorded
Audit authority: none
Commits: exactly one, as specified

## Stopping Conditions

Stop with `PARTIAL` or `BLOCKED` if any gate fails; the status set or digest differs from the accepted candidate; an unexpected path appears; the commit would include content outside the candidate; a secret-like value appears; the remote has advanced or requires force; credentials or host details would be exposed; or any operation beyond the exact sequence is needed. Do not improvise recovery.

## Terminal Report

Write atomically to `/home/agile/meta/projects/libretiles/18/00-dockerized-vps-deployment/08_report_00.md`. Begin exactly:

`### Report for ORCHESTRATOR_CHAT`

Echo exactly once: Logical whole identity: dockerized-vps-deployment, Worker session ordinal: 08, Worker exchange ordinal: 01.

Include:

- terminal status `PASS`, `PARTIAL`, or `BLOCKED`;
- Phase-qualified result: `publication-PASS` only if the exact commit is the public `refs/heads/main` and direct readback matches, otherwise `not-applicable`;
- Result artifact or commit: the exact published commit SHA;
- Result evidence: gate results, staged path count, commit parent, clean status, push result, direct public readback;
- Logical-whole closure: not-closed;
- deviations, missing evidence, and residual risks;
- one smallest next step for the Orchestrator (closure remains ORCHESTRATOR-owned);
- Report justification: new-mutation;
- Authority expiry: publication authority expires when the report is written; no further Git write, deployment, production, or closure authority remains.

The Worker must not deploy, must not close the logical whole, and must not claim deployment PASS or production acceptance.

Report justification: new-mutation
