Artifact class: **evidence deposit written by another whole's Orchestrator.** Not authority, not a
handout, not a plan. Logical whole `admin-provider-model-console` (Meta 11/00).

Written on 2026-09-02 by the era-10 `ui-internationalization` Orchestrator at the Cooperator's explicit
instruction: *"daj B21 do backlogu pripadne vytvor na zaklade vsetkeho co sa tyka admin rozhrania chcem v
logickom celku v meta libretiles/11/00-admin-provider-model-console tam budem riesit vsetko ohladom
admina takze daj tam aj toto, ze je NOT TESTED ... Freeze B21"*.

⛔ **`00_handout.md` in this directory was NOT read.** The Cooperator's standing instruction to the
era-10 Orchestrator is not to read the handouts in `10/00-product-acceptance-sweep/`,
`10/01-player-model-choice-removal/` or `11/00-admin-provider-model-console/`, to avoid a loop. This file
was written blind to that handout. If anything here duplicates or contradicts it, **the handout is this
whole's own artifact and wins**; treat this file as an independent measurement deposit to reconcile.

Filename uses a `9N_` prefix so it can never collide with a Worker-session ordinal, mirroring the
convention documented in `10/00-ui-internationalization/90_orchestrator-restoration.md`.

---

# 1. Why this file exists

Logical whole `10/00 ui-internationalization` delivered `R6` — the player-facing model and prompt
pickers are gone — at commit `383011b389a9b3690647b6fa673060633572ab9d`. Verifying it required measuring
the admin surface, and the Cooperator then correctly ruled that admin verification is **not part of
`10/00`**:

> *"teraz dokoncme prosim tvoj logicky celok, admin bola odbocka, je to najdolezitejsie pre mna okrem
> hry proti AI a lokalizacia + UI/UX perfektne.. Toto sa ale netyka tvojho logickeho celku"*

So the measurements are deposited here instead of being lost, and the acceptance batch is **frozen**.

# 2. FROZEN acceptance batch B21 — status NOT TESTED

Batch `B21` was drafted for the Cooperator and then frozen at his instruction before he ran it. **Every
item below is `NOT TESTED`.** It is carried here as ready-made acceptance material for this whole, not as
an open obligation on `10/00`.

```text
B21-1  NOT TESTED   open http://127.0.0.1:8000/admin/ and log in as the existing superuser
B21-2  NOT TESTED   PER-USER PREFERENCE: Users -> admin -> change "preferred ai model id" to another
                    eligible id, save, start a NEW AI game, confirm the header and draw pill show it
B21-3  NOT TESTED   GLOBAL DEFAULT: (a) CLEAR "preferred ai model id" on the user first — mandatory,
                    see section 5 — (b) confirm the resolved model falls back to catalog row 1,
                    (c) Catalog -> AI models -> change a `sort_order` so a different row is first,
                    (d) start a NEW AI game and confirm it plays that model
B21-4  NOT TESTED   PROMPTS: Catalog -> AI prompts -> change a `sort_order`, start a new game, and
                    verify via Admin -> Game sessions -> newest session -> "ai prompt", because the
                    prompt is deliberately invisible to the player after R6
B21-5  NOT TESTED   the R6 UI leftovers: settings shows a name only, no "Choose AI" on /play, the draw
                    pill shows a name not a raw id, and the game header has no prompt control
```

An earlier attempt at `B21-1`'s predecessor (`B20-6`) returned FAIL, and that FAIL was an **Orchestrator
instruction defect, not a product defect**: the batch said "Django Admin (/admin/)" without a port and the
Cooperator reasonably tried `localhost:3000/admin`, which is the Next.js frontend and correctly 404s.
Django admin is on **port 8000**. Recorded so this whole does not re-inherit a phantom failure.

# 3. Measured admin-surface facts, at `383011b`

All of this is `reproduced-dynamic` or `established-static`, measured by the era-10 Orchestrator against
the live development database and the installed source. **Re-verify before relying on any of it** — the
catalog is data and the Cooperator plays with it.

## 3.1 Reachability and identity

```text
ss -tlnp            127.0.0.1:8000  python (Django)        *:3000  next-server (v16.3.4)
GET http://127.0.0.1:8000/admin/    -> 302 -> /admin/login/?next=/admin/ -> 200, 4173 B
                                       <title>Log in | Django site admin</title>
Next.js app routes  /  ·  /play  ·  /settings  plus /draw/[id] /game/[id] /waiting/[id]
                    there is NO /admin route on the frontend and there should not be
superuser           EXISTS — id=1, username 'admin', is_staff=True, is_superuser=True
users total         4:  id=1 admin · id=2 liveplay06w · id=3 hrac · id=4 hmm
```

Django admin is **session**-authenticated while the API is JWT-authenticated, so admin cookies are real
credentials; that is already recorded in `PROJECT_CONTEXT.md` section 7 and matters for any admin work.
The Django admin login form is **not** a DRF view, so the DRF throttles do not protect it —
`django-axes` does, with `AXES_FAILURE_LIMIT = 8` and a 30-minute cooloff stored in the **database**, so a
Django restart does NOT clear a lockout. Delete the `AccessAttempt` row in admin instead.

## 3.2 The catalog as it actually stands

```text
AIModel rows (sort_order, model_id, is_active):
     1  openai/gpt-oss-120b                         active=False
     2  gemini-3.7-flash                            active=False
     3  @cf/zai-org/glm-4.7-flash                   active=False
     4  mistral-small-2603                          active=False
     5  ibm/granite-4-h-small                       active=False
    10  google/gemma-4-31b-it:free                  active=True
    20  nvidia/nemotron-3-super-120b-a12b           active=True
    30  nvidia/nemotron-3-super-120b-a12b:free      active=True
    40  z-ai/glm-5.2:free                           active=True
    50  google/gemma-4-26b-a4b-it:free              active=True
   100  aion-labs/aion-3.0-mini                     active=False
   110  openai/gpt-oss-120b:groq                    active=False

get_selectable_models()   -> 5 rows, ROW 1 = google/gemma-4-31b-it:free

AIPrompt rows:
     5  Grandmaster   active=True
    10  Initial       active=True
    20  Fast Search   active=True
    30  Short Hooks   active=True

get_selectable_prompts()  -> 4 rows, ROW 1 = Grandmaster
```

Note that the seven inactive rows are the extra providers. `is_active` is the durable kill switch and
neither `seed_models` nor `sync_openrouter_models` may flip it — that is a standing rule in `AGENTS.md`.

## 3.3 ✅ The admin CAN already set the default, and the plan understated this

```text
backend/catalog/models.py      both AIModel and AIPrompt order by ("sort_order", ...)
backend/catalog/admin.py:43    AIModel   list_editable = ("is_active", "sort_order")
backend/catalog/admin.py:113   AIPrompt  list_editable = ("fitness", "is_active", "sort_order")
backend/game/services.py:366-384  _resolve_ai_model:  field omitted -> selectable_models[0]
backend/game/services.py:386-393  _resolve_ai_prompt: field omitted -> selectable_prompts[0]
backend/game/serializers.py:174-175  BOTH fields are required=False
```

So **row 1 is admin-settable today by editing `sort_order` inline**, with no code change and no SSH, and
after `R6` the frontend omits both fields so row 1 is what a new game uses.
`92_orchestrator-glossary-and-plan.md` slice S4 said this "does NOT deliver 'the admin sets the GLOBAL
default', which is still catalog row 1 determined in code". That claim is **too pessimistic** and is
corrected here.

⚠ One honest caveat: that holds while `DYNAMIC_FREE_MODEL_CATALOG_ENABLED` is `false`, which is the
default in `backend/config/settings.py`. With the flag ON, model ordering is by release date and the
administrator influences row 1 only through `is_active`. Any admin-console design that promises
"reorder to set the default" must say which flag state it assumes.

# 4. What `R6` already delivered, so this whole does not rebuild it

Landed at `383011b`, Orchestrator-verified, **zero backend change** (`git diff --name-only -- backend/`
returned 0 files, 0 migrations):

```text
GONE   the selectable rival panel in Settings — now a read-only display_name
GONE   "Choose AI" on /play and the raw model id on /draw/[id] — both show a display name
GONE   the entire prompt-preset surface: the switch effect, the ScorePanel control,
       `selectedPromptId` (persist 4 -> 5 with a migration), and both picker components,
       PromptCatalogModal.tsx and PromptPreviewModal.tsx, which were DELETED
GONE   `ai_prompt_id` from the createGame request, so the backend picks prompt row 1
KEPT   accounts.User.preferred_ai_model_id, its migrations, its admin field, and its
       is_selectable_model validation in accounts/serializers.py:52-55
KEPT   `selectedModelId` in the frontend store — see section 5, it is load-bearing
```

Cooperator-verified rendered evidence: batch `B20-5` PASS — an AI game still plays normally after the
pickers were removed.

# 5. ⛔ TWO TRAPS this whole must not walk into

## 5.1 The resolution precedence makes a naive "reorder and see" test invalid

`frontend/src/lib/model-catalog.ts:95-103`, read from source:

```ts
if (preferredId && eligibleIds.includes(preferredId)) return preferredId;   // per-user
if (storedId    && eligibleIds.includes(storedId))    return storedId;      // this device
return eligibleIds[0] ?? null;                                             // catalog row 1
```

The live database has `admin.preferred_ai_model_id = 'nvidia/nemotron-3-super-120b-a12b'`, which is
active and eligible. **So reordering `sort_order` while logged in as `admin` changes row 1 and changes
nothing about that user's game.** An observer would see "no effect" and conclude the admin control does
not work, when in fact a higher-precedence per-user preference — itself admin-settable — is winning.

Any admin-console acceptance test must either clear the per-user preference first or test the per-user
path deliberately. `B21-3(a)` exists solely because of this.

## 5.2 `selectedModelId` is not a picker value and must never be deleted

```text
frontend/src/app/game/[id]/page.tsx:833   preferenceModelId = selectedModelId || gameState.ai_model_id || ""
frontend/src/lib/ai-fallback.ts:90-96     that preference becomes ATTEMPT 1 of the provider fallback queue
```

Deleting it would break every AI turn **while leaving all eight standing gates green**, because no test
exercises the queue's preference input. `R6` kept it deliberately: the player stopped *choosing*, the
value did not stop *existing*.

# 6. Open items this whole inherits from `10/00`

```text
uii-01-F13   `api.getPrompts` and the Next.js `/api/prompts` proxy now have ZERO callers after R6
             deleted the prompt picker. The build still lists `ƒ /api/prompts`. It is one of the two
             catalog proxies in `audit-01-F06`, which `10/00` slice R11 owns, and R11 must decide there
             whether to delete them or keep them FOR THIS WHOLE. If this whole wants a prompt list in
             an admin surface, say so before R11 runs.
             ⛔ Do NOT delete the Django `catalog/prompts/` endpoint — an admin console needs it.
Strength     PROJECT_CONTEXT.md section 12 records his intent to test a model's strength before
metric       promoting it to default, and section 6 constrains how: final score is an ENGINE number and
             is identical whichever model is plugged in, so a strength metric must rest on the
             `completion_source` distribution and the `provider_candidate` rate. Measured reality: the
             free LLM has authored ZERO backend-valid placements across roughly a dozen counted live
             invocations, so `provider_candidate` is currently 0 for every model. A strength dashboard
             that cannot say "I did not measure" would be worse than none.
Providers    Locked fork 11 freezes all nine providers pending this whole. Nothing in `10/00` touched
             any provider list, constant, tier, model tuple, or provider documentation, and every slice
             report asserted that explicitly.
```

# 7. What this file is not

It grants no authority. It is not a plan, not a handout, and not acceptance evidence for anything. Every
number in it is a measurement at `383011b` on the Cooperator's development machine and must be re-taken
before use. `B21` is **frozen and NOT TESTED**, at his explicit instruction, and no part of `10/00`
depends on it.
