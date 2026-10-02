# S10 Preflight Record — Public rename scope and sequence (Orchestrator-authored, read-only)

Logical whole identity: kronika-one-product
Worker session ordinal: 68
Worker exchange ordinal: 01
Author: ORCHESTRATOR (direct read-only preflight under the Cooperator’s
  authorization; no Worker exchange)
Phase: preflight
Task identity: KRONIKA-ONE-PRODUCT-S10-PREFLIGHT
Baseline: 2af8edde5faf8967777a68b0a72685cc580c45ea (public main and NUC)

## Verified current state (2026-10-01)

- Local checkout `feat/kronika-one-product` clean at `2af8edd…`; `origin` =
  `https://github.com/cisarik/framenest.git`.
- `cisarik/kronika` (the former capture repository) has exactly `HEAD` /
  `refs/heads/main` at `66c40d43c577276b0ad304a494fbbb1ffb6fc933`.
- `cisarik/framenest` public refs: `main` = `feat/kronika-one-product` =
  `2af8edd…`; the two parked heads unchanged (`26d28b16…`, `7ff6546f…`).
- The release helper `deploy/ubuntu/framenest_release.py` verifies public main
  via `git ls-remote origin refs/heads/main`, i.e. through the local remote
  name, not a hardcoded URL.

## Live references to the old repository identity

| Location | Count | Class | S10 action |
|---|---|---|---|
| `deploy/systemd/*.service`, `*.timer` `Documentation=https://github.com/cisarik/framenest` | 10 | live documentation URL | update to `https://github.com/cisarik/kronika` |
| Local Git remote `origin` | 1 | machine config | update after the GitHub rename |
| `ap.project.conf` `projectId = cisarik/framenest` + `tests/contract/test_ap_project_contract.py` | 1 | internal AP consumer identity | keep (AGENTS: internal package, migration history, deployment identifiers remain; no mass rename) |
| `docs/provenance/kronika-capture.json` + `tests/contract/test_chatgpt_page_packaging.py` | historical provenance manifest | historical evidence | keep (records the source at capture time; GitHub redirects old URLs) |
| ADRs / trace | historical text | historical | keep |

No README/PRODUCT/SPEC/SERVER/ROADMAP live link references the repository URL.
No other code, configuration, helper, unit or test depends on the repository
name. The capture units’ `Documentation=` lines are cosmetic; installed host
units keep the old text until a later reinstall and require no functional
change.

## Exact sequence

1. **Cooperator (GitHub account authority), in this order:**
   rename `cisarik/kronika` → `cisarik/kronika-capture-archive` (frees the
   name), then rename `cisarik/framenest` → `cisarik/kronika`. No transfer,
   visibility change, force or history operation; GitHub keeps redirects from
   the old names.
2. **Bounded reference-update grant (direct execution under the Cooperator’s
   S10 authorization):** update the local `origin` to
   `https://github.com/cisarik/kronika.git`; update the ten unit
   `Documentation=` URLs; one local commit
   `chore: update repository URLs for the kronika rename`; non-force
   fast-forward push of `main` and `feat/kronika-one-product` to the renamed
   repository; direct readback.
3. **Verification:** new-repository refs equal the published commit; old-name
   redirect resolves to the same refs; `cisarik/kronika-capture-archive`
   still reads `66c40d43…`; routine NUC capability: `framenest-release check`
   continues to work from the updated local remote (no NUC mutation needed;
   installed unit `Documentation=` text is cosmetic).
4. **Archive last (Cooperator):** after verification, archive
   `cisarik/kronika-capture-archive` in GitHub settings.
5. **S10 acceptance record**, then whole-closure evaluation.

## Risks and boundaries

- No history rewrite, no force push, no repository deletion or transfer; the
  parked capture repository is untouched until the rename and is archived
  only after verification.
- Internal identifiers (`framenest` package, unit names, AP projectId,
  migration history, HTTP headers, helper name) remain; S10 changes only the
  public repository names and their live URL references.
- The trace (Meta) remains historical and is not part of the rename.
