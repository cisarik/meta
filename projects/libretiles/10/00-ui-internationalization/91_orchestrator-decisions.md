Artifact class: **Orchestrator-authored decision and evidence record**, not a Worker exchange and not
authority. Logical whole `ui-internationalization` (Meta 10/00). Filename deviation is explained in
`90_orchestrator-restoration.md`. Worker-session ordinal `01` remains unused.

The durable owner of decisions 1–6 below is `PROJECT_CONTEXT.md` section 13, and of the admin-console
product intent is `PROJECT_CONTEXT.md` section 12. This file records the exchange that produced them
and is deliberately not a second copy of their content.

---

# Opening decision exchange — 2026-09-01

## What was presented

A six-item decision package, each item carrying one recommendation and the evidence behind it:

```text
1  locale routing            path prefix (recommended) | subdomain
2  interface locale switch   Settings + first-visit browser detection (recommended) | switch only |
                             detection only
3  Slovak register           ty / tykanie (recommended) | vy / vykanie
4  nonce CSP (orch-01-F18)   implement (recommended) | leave the residual with its sign-off
5  Django HSTS (orch-02-D11) includeSubDomains yes, preload no (recommended) | leave both
6  sequencing                Deep Research prompt first (recommended) | localization first
```

Recommendation 1 explicitly argued **against** the "subdomain-locale feature" that the era-09 handout
had named, and said so as such rather than quietly dropping it.

## What he decided

Verbatim: `1.) A 2.) A 3.) A 4.) A 5.) A  6.) B`.

So options A on the first five, exactly as recommended. On item 6 he chose B — localization first — and
then qualified it in the same message, which is what makes item 6 worth recording carefully rather than
as a single letter.

### Item 6, reconciled

His qualification, verbatim in substance: he does want the VPS-deploy Orchestrator handout **and** the
Deep Research prompt written — *"Prompt ktorý k VPS deploy logickému celku napíše všetko potrebné a áno
aj prompt pre Deep Research potrebujeme prompt"* — but he is not doing the deployment yet, because he
plans UI/UX changes before it.

Reconciled reading, and the one that was put back to him for confirmation in a single line rather than
assumed: **both artifacts remain owed and are not cancelled; only their delivery is no longer first in
line, and the deployment act itself waits for the UI/UX work.** The carried-forward obligation in
`PROJECT_CONTEXT.md` section 11 therefore stands unchanged.

This matters because `PROJECT_CONTEXT.md` section 2 records that one one-word reply was once misread and
cost an entire Worker session. `B` alone would have read as "do not write them".

## What he raised unprompted, and it is the more important half of the message

He named the other logical wholes still outstanding — `10/00-product-acceptance-sweep`,
`10/01-player-model-choice-removal`, and **especially** `11/00-admin-provider-model-console` — and gave
an explicit instruction:

> NECITAJ ALE HANDOUTY ABY NENASTAL LOOP SU TAM HANDOUT PROMPTY

**Complied with strictly.** None of those three handout files has been opened by this Orchestrator. The
directory listing was already visible from a `ls` performed during Stage 1, before the instruction
existed; no content was read then and none has been read since. Everything recorded about those wholes
comes from `PROJECT_CONTEXT.md`, `DEFECT_LEDGER.md`, `09/00-backend-security-hardening/99_closure.md`,
`AGENTS.md`, and the repository itself.

He then asked whether his brainstorming about the ideal admin interface and about models not being
hardcoded had been lost.

### The honest answer, and the action taken

The **decision** was not lost: locked fork 11 in `PROJECT_CONTEXT.md` and the 2026-08-31 entry in
`DEFECT_LEDGER.md` both record that the nine providers are frozen pending a dedicated whole, in his own
words, "change nothing and revert nothing".

The **detail** was not in `PROJECT_CONTEXT.md` at all. Locked fork 11 says nothing about an admin UI
shape, nothing about AI-vs-AI diagnostics, nothing about strength-testing a model before promoting it to
default, and nothing about the player seeing only a model name. `AGENTS.md` names
`admin-provider-model-console` as a later whole with no detail. So his worry was **justified**: had that
detail existed only inside the `11/00` handout, and had a future Orchestrator been told not to read it,
it would have been unreachable.

Action taken: the detail he restated in this message is now written into `PROJECT_CONTEXT.md` section 12
as durable product intent, in the same deliberate way section 11 carries the deployment obligation —
"recorded here, not only in a handout, so it cannot be lost when a session ends". It is recorded as
intent, not as authority to implement.

## Factual correction owed to him, verified in the repository

He wrote *"Frontend už je snáď zmenený a user má vedieť len názov modelu"*. It is not. Verified at
`19cfec9` by direct reading, not inferred:

```text
frontend/src/app/settings/page.tsx:656-712   selectable rival panel over the live catalog
frontend/src/app/settings/page.tsx:664       "No rival selected"
frontend/src/app/play/page.tsx:31,65         "Choose AI"
frontend/src/hooks/useGameStore.ts:30,129    persisted selectedModelId, default ""
frontend/src/hooks/useGameStore.ts:32,131    persisted selectedPromptId
frontend/src/components/game/ScorePanel.tsx:425   "Prompt: {label}" / "Prompt presets"
frontend/src/components/game/PromptCatalogModal.tsx                a full prompt-preset picker
```

Two player-facing internals exist, not one: the **model** choice and the **prompt-preset** choice. The
prompt-preset picker arguably leaks more product internals to a player than the model picker does.
`10/01-player-model-choice-removal` is therefore real outstanding work.

## Sequencing observation put to him as a scope question

Removing the player's model and prompt choice rewrites `frontend/src/app/settings/page.tsx` (803 lines),
which is the same file this whole rewrites for the interface-locale switch and the two-axes relabelling
of `GameLanguagePanel`. Two wholes rewriting one file in sequence produces avoidable churn and two
review passes over the same diff surface.

Recommendation put to him: fold the **frontend half** of his top priority — removing the model and
prompt pickers so the player sees only a model name — into this whole's Settings rewrite, and leave the
**admin half** (provider and model CRUD in Django admin, default selection, AI-vs-AI diagnostics in both
variants, strength testing before promotion) as its own whole with a clean boundary. That gives him part
of his stated most-important outcome now and at almost no extra cost, without reopening locked fork 11,
which freezes provider *lists and constants* rather than the player-facing *pickers*.

Not decided. It is a scope change and therefore his.

## Locked-fork check performed before making that recommendation

Locked fork 11 freezes "any provider list, provider constant, provider tier, exact model tuple, or
provider documentation" in `provider-registry.ts`, `openai-compatible.ts`, `selection.py`, `README.md`,
and `AGENTS.md`. Removing a *player-facing picker* in `settings/page.tsx`, `play/page.tsx`, and
`useGameStore.ts` changes none of those five files and adds, removes, or renames no provider. The
recommendation is compatible with the freeze. Stated explicitly because assuming it would be exactly the
kind of unchecked inference this project has been bitten by.

## State at the end of this exchange

```text
Active mutation      none
Active Worker        none
Worker prompts issued  none
Repository changes   none — porcelain still empty at 19cfec9
Meta writes          90_orchestrator-restoration.md, this file, PROJECT_CONTEXT.md sections 12 and 13,
                     DEFECT_LEDGER.md era-10 section. Meta is NOT committed by the Orchestrator.
Open on him          the npm run build gate needs his dev server stopped; locale persistence
                     (device vs account); the fold-in scope question above
```
