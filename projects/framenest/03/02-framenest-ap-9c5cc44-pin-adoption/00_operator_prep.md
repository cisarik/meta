# Operator prep — FrameNest AP 9c5cc44 pin adoption

```text
Logical whole identity: framenest-ap-9c5cc44-pin-adoption
Execution: Cooperator-authorized operator path (no Worker)
Date: 2026-08-16
```

This folder records the FrameNest pin adoption that the closed AP whole
`ap-consumer-declared-execution-route-and-capability-gate-binding` left outside
its own closure: FrameNest gitlink, public main, NUC routine deploy, and Meta
archival. Product work is not in this identity.

## Why no Worker

The Cooperator asked for a clean primary checkout, current AP pin, current
public `main`, and current NUC before opening a separate FrameNest product
whole with a ChatGPT readonly Worker. Pin apply, gitlink commit, ordinary
push, and `framenest-release deploy` were executed on that operator path.

## Checkout cleanup (primary tree only)

Removed from `/home/agile/Projects/framenest`:

- nested worktrees `.accept-immut-work/` and `.w6-immut-work/`
- `.playwright-mcp/`
- accidental `REPRO_DIR=` directory
- untracked `uv.lock`
- fully merged local branch `fix/cursor-worker-execution-boundary`

Not removed: ~40 leftover Worker worktrees under `~/Projects/framenest-*` and
`~/Projects/framenest-worktrees/`. They are outside the primary checkout and
outside a fresh GitHub clone.

## AP pin

```text
Old pin: 17b7e085139e9bcbb0e4953d26aef9b6687d541c
New pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
```

Forward AP commits in the pin:

```text
1cd2783 docs: extend existing RF families for cost-proportional Worker grants
95bd644 docs: mark ADR-0017 accepted
10ac2ed docs: bind Worker prompts to declared routes
9c5cc44 docs: mark ADR-0018 accepted
```

Validation:

```text
./.ap/ap update --apply
./.ap/ap doctor --candidate  → PASS
./.ap/ap project check --root /home/agile/Projects/framenest --candidate → PASS (non-authorizing)
git add .ap && ./.ap/ap doctor → PASS, governing variant stable
./.ap/ap project check --root /home/agile/Projects/framenest --baseline 3cf22b8aaff61ed71093207d5b24aae622f394ac → PASS
```
