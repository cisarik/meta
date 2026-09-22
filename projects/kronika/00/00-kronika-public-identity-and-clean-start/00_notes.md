# Era 00 Whole Notes — Kronika public identity and clean start

Classification: private local historical/evidentiary projection for this
logical whole. Orchestrator-owned after restore, append-only during the whole,
frozen at closure. Non-authorizing. Public-safe by default. Michal owns any
meta Git commit.

Working identity (Cooperator-selected 2026-09-22, pending Planner lock of the
exact slice boundary):

```text
kronika-public-identity-and-clean-start
```

Trace:

```text
/home/agile/meta/projects/kronika/00/00-kronika-public-identity-and-clean-start/
```

Handout: `00_handout.md` (2026-09-22). Live for the incoming fresh Orchestrator.
Not Worker authority.

Lab checkout (not yet the public product repo):

```text
/home/agile/Tools/cli_chatgpt
branch main
HEAD 2727451d2502925377637e19fa435917c970a996
no Git remote
AP pin 7478ddb07d2c3911f79e1aa1441f0115a31c45d8
```

## Session log

- **2026-09-22 — Cooperator brainstorm (pre-Orchestrator).** Product restart
  from the private `cli_chatgpt` lab: Kronika is a household chronicle of
  web searches and deep research worth returning to, not chat history and not
  a group chat. One household ChatGPT Plus/Pro account does capture. Family
  members keep using existing chat channels. Authorship (follow-up prompt into
  an existing record) and `library check` stay. Notification/watch/group-chat
  framing is a dead end. ChatGPT project `web` is scratch; Kronika is the
  archive. Android Chrome extension is rejected (platform does not support it).
  Family access is Tailscale, same pattern as the household NUC. Later:
  lightweight native Android/iOS share targets; desktop Chrome extension as
  family-admin surface. Public GitHub from day one for a professional
  open-source interview artifact. Empty GitHub repo first; first push only
  after a clean identity tree. Meta starts at this directory.

## Locked Cooperator decisions (intent, not ADR)

1. **Product name:** Kronika. GitHub repo `cisarik/kronika`, public.
2. **Audience:** one household. Shared capture account is a household choice,
   not a public multi-tenant product.
3. **What Kronika is:** durable shared library of searches and deep research
   the family wants to reopen. Opt-in share only.
4. **What Kronika is not:** ChatGPT history dump, group chat, notification
   inbox, or a replacement for Signal/mail/family chat.
5. **Keep:** capture of web search and deep research; local SQLite library;
   manager UI; Private vs shared; follow-up authoring; `library check`.
6. **Drop from the public story and, where cheap, from the tree:** doctor /
   diagnostics / recover stubs; Obscura; encyclopedic experiment ROADMAP;
   watch/scheduler (already removed); group-chat framing.
7. **Family client:** web library over Tailscale. Not an Android Chrome
   extension.
8. **Native share (horizon, not this whole):** Android and iPhone
   “Share to Kronika” as a lightweight share-target app. Later they talk to
   the same Tailscale web surface.
9. **Desktop extension (horizon, not this whole):** family-admin / capture
   surface for the household head, not the family viewer.
10. **ChatGPT project `web`:** scratch. Auto-delete of remote conversations is
    later; not this whole.
11. **Public Git history:** do **not** publish the 190-commit `cli_chatgpt`
    lab log. Public `main` starts clean (orphan / first-commit of the cleaned
    tree). Keep the lab history locally as a non-pushed branch.
12. **GitHub create:** Cooperator creates an **empty** public repo (no GitHub
    README, gitignore, or LICENSE). No push until this whole produces the
    cleaned tree.
13. **ToS posture in public docs:** honest experimental unofficial tool;
    may conflict with ChatGPT terms; AS IS; no warranty; no affiliation with
    OpenAI. A disclaimer is not a ToS license.
14. **External analytic trace:** this Meta project `kronika` is now in use.
15. **First Worker of the incoming Orchestrator:** Planner, native plan mode,
    this whole only.

## Recommended first product whole after this one (not authorized)

```text
kronika-tailnet-family-library
```

Family members open the library from phones over Tailscale. That is the first
family-testable behavior. Native share apps need that reachable surface first.

## Open gates for the incoming Orchestrator

- Confirm `cisarik/kronika` is the GitHub identity once the empty repo exists.
- Planner must bound: user-facing rename vs Python package `chatgpt_cli`
  rename vs XDG state-dir break. Recommendation in the handout.
- `docs/environment.md` contains a household ChatGPT project URL and local
  paths; it must not ship as public professional documentation.
- `docs/security.md` is an experiment ledger (~2000 lines); public
  `SECURITY.md` must be short.
- Publication push is Cooperator-owned even after the tree is clean.
- Do not implement Tailscale bind, native apps, or remote listen in this whole.
