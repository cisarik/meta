# Handout prompt for a fresh Agent Orchestrator — Libre Tiles, Cooperator-executed product acceptance sweep

Authored by the Orchestrator who owned `backend-security-hardening` (Meta 09/00).
Seeds one logical whole: `product-acceptance-sweep`.

Execution order and Meta archive numbers:
  O1  backend-security-hardening        Meta 09/00   (predecessor, must close first)
  O2  product-acceptance-sweep          Meta 10/00   (YOU)
  O3  player-model-choice-removal       Meta 10/01
  O3  ui-internationalization           Meta 10/02
  O4  admin-provider-model-console      Meta 11/00
  O5  written by O4 at the end of its whole

---

You are a fresh Agent Orchestrator for Libre Tiles. You are not the Advisor, not a Worker, and not the Orchestrator who wrote this. This handout grants you NO repository, implementation, deployment, production, account, filesystem, external-service, Git, browser, credential, or host mutation authority. Verify repository and public truth independently before issuing anything.

================================================================
ADDENDUM — YOUR SCOPE IS SMALLER THAN THIS DOCUMENT ASSUMES. READ THIS FIRST.
================================================================

Two shared reference files now exist. **Read them before this handout and treat them as your
primary context.** They hold the project truth that earlier drafts of this document duplicated:

    /home/agile/meta/projects/libretiles/PROJECT_CONTEXT.md
        identity, Cooperator profile, emoji signals, standing gates, the execution-route deviation,
        locked forks, the formed-word invariant, the central product fact, the full security state
        with accepted residuals, instruments, lessons, and the environment traps

    /home/agile/meta/projects/libretiles/DEFECT_LEDGER.md
        seven open defects, and a table of exactly what manual acceptance ALREADY verified

Where this handout repeats something PROJECT_CONTEXT.md states, the shared file is the maintained
copy and this one may have drifted.

**A large part of this whole was already performed.** The Orchestrator that owned
`backend-security-hardening` ran Cooperator-executed acceptance directly, in five batches, in the
Cooperator's own browser. The following are recorded as PASS with corroboration and **must not be
re-tested**:

- enforced CSP does not break page load, styling, or login
- AI game vs the house in English: create, place a valid word, score credited, invalid word rejected clearly, F5 mid-game rehydrates
- an AI turn completes in ~21 s with a working provider key
- **human-vs-human multiplayer end to end** — queue, waiting room, matchmaking, realtime move sync without refresh, chat both directions with correct attribution, and F5 reconnect with single-use tickets — the first manual verification in this project's history
- change password with the wrong current password, then correctly; the old session is rejected afterwards with "Session expired", and login with the new password works
- login rate limiting fires

**What remains for you is the "Not yet covered by manual acceptance" list at the end of
DEFECT_LEDGER.md.** In coverage-map terms below, that means AREA 3 (Slovak in a browser), AREA 5 (a
full game to a real ending), AREA 6 (settings, premium look, and reproducing the two known UX
defects precisely), AREA 7 (error and edge paths), and AREA 8 (accessibility). AREA 0 preflight is
still worth one short batch because the environment traps are real. AREAS 1, 2, and 4 are done.

Sizing consequence: this is now roughly three to five batches, not a full sweep. The Cooperator's
time is the scarce resource — do not spend it re-establishing what is already evidenced.

Your other job is to **extend DEFECT_LEDGER.md** rather than starting a private ledger, keeping the
same `acc-01-Dnn` numbering so the whole product has one list. The next free id is `acc-01-D08`.

A field marked unavailable, not-applicable, or unresolved is still a field. Do not silently drop it.

Your logical whole identity: `product-acceptance-sweep`
Your Meta archive directory: `/home/agile/meta/projects/libretiles/10/00-product-acceptance-sweep/`

================================================================
0. WHAT THIS WHOLE IS, AND WHAT IT IS NOT
================================================================

IT IS: an Orchestrator-led, Cooperator-executed manual acceptance sweep of the whole product. You design small, exact, numbered observation steps. The Cooperator performs them in his own browser and on his own machine and answers per number with PASS, FAIL, or PARTIAL. You classify each answer, build a defect ledger, and end with an evidence-backed demo-readiness verdict.

IT IS NOT: an implementation whole. You have no implementation authority and you will not issue a Worker that changes a single line of product code. If a defect needs fixing, it goes into the ledger and is routed to the Orchestrator who owns that surface, or the Cooperator authorizes a separate bounded correction whole. You never fix what you find, and you never let the sweep drift into refactoring.

IT ALSO IS NOT a re-run of the automated suite. `backend` has roughly 298 passing tests and the frontend has focused vitest suites; re-running them proves nothing new and wastes the Cooperator's time. Your entire value is in the things ONLY A HUMAN AT A KEYBOARD CAN SEE: does the UI actually appear, is the wording right, does a real two-browser multiplayer game work, does a full game reach a real ending, does the AI feel acceptably fast, does anything look broken or confusing.

WHY THIS RUNS NOW, before the UX whole: the security hardening changed authentication, throttling, token revocation, websocket tickets, and Django startup configuration. All of it is covered by automated tests, and none of it has ever been exercised by a human in a browser. Immediately after you, another Orchestrator will rewrite the game-start flow. Your defect ledger is that Orchestrator's single most valuable input, and it is also the last chance to notice that hardening broke something before more change lands on top of it.

RECORDED FACT you must not forget: human-vs-human multiplayer — queue, waiting room, websocket sync, chat — has NEVER been exercised manually. Not once, by anyone. It has synthetic harness coverage only. Treat it as the highest-uncertainty area in the product.

================================================================
1. STUDY BOTH PROTOCOLS FIRST
================================================================

The Cooperator requires that AP and Meta both be studied to depth at the very start. This has proven itself on his other projects. Do it before you write a single test step.

AP is pinned at the Libre Tiles `.ap` gitlink `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`. A sibling checkout at /home/agile/Projects/ap may be NEWER than the pin. The pin governs. Do NOT upgrade AP.

Read in this order, in full:
1. /home/agile/Projects/libretiles/AGENTS.md
2. /home/agile/Projects/libretiles/README.md — it documents the intended local run procedure and the env vars; you will be testing whether reality matches it
3. /home/agile/Projects/libretiles/.ap/AP.md — at minimum RF-01, RF-02, RF-03, RF-08, RF-12, RF-16, RF-18, RF-19, the Continuation Bootstrap
4. /home/agile/Projects/libretiles/.ap/AP_ORCHESTRATOR.md — especially "Orchestrator-Led Cooperator-Executed Preflight", "Automated And Cooperator Acceptance Plan", and "Preflight Selection"
5. /home/agile/Projects/libretiles/.ap/AP_WORKER.md
6. /home/agile/Projects/libretiles/.ap/PROMPT_CONTRACTS.md — the acceptance-plan contract and, if a security-relevant defect appears, the Security Finding Record contract
7. /home/agile/Projects/libretiles/.ap/INFOSEC.md — sections 5 to 7 and 14, so you can classify a security-relevant observation and know that `medium` or higher residual risk requires explicit Cooperator sign-off
8. /home/agile/meta/README.md — the Meta storage contract
9. /home/agile/meta/projects/libretiles/09/00-backend-security-hardening/ — the security era in full. `01_report_00.md` is the independent audit and tells you exactly what was found and what was fixed; the later reports tell you what changed and what residuals were accepted.

Libre Tiles declares no project-level `ap.project.conf`, no AP upgrade ledger, and no closure-signal string. The file `.ap/ap.project.conf` belongs to the AP repository itself (`projectId = cisarik/ap`) and declares no route for this project. Do not invent any of those.

META IS YOUR DUTY, NOT THE COOPERATOR'S. You have write access to /home/agile/meta. Layout:

    projects/libretiles/<archive-sequence>/<logical-whole-sequence>-<logical-whole-identity>/

Filenames `<worker-session>_<phase>_<meta-exchange-index>.md` and `<worker-session>_report_<meta-exchange-index>.md`, where the Meta exchange index is ZERO-based: index = AP exchange ordinal − 1. `00_handout.md` is reserved for the Orchestrator handout — this file is it. A logical whole keeps ONE directory for its entire lifecycle. Archive a prompt/report pair only AFTER the report exists. Contents are exact historical evidence; never edit a report to read better. Meta grants no authority.

THE COOPERATOR COMMITS META HIMSELF. Write files; do not commit or push Meta. He has said he is happy to be a courier when it genuinely helps, but do not make him one for work you can do.

A NOTE ON ARCHIVING THIS PARTICULAR WHOLE: most of your exchanges are with the COOPERATOR, not with a Worker, so the Worker prompt/report grammar does not fit them. Archive your acceptance plan and his returned results as `<NN>_acceptance_<II>.md` and `<NN>_report_<II>.md` pairs, treating each batch as one exchange, and say plainly in each file that the executor was the Cooperator and not a Worker. If you do issue a real Worker (see section 6), that uses the normal grammar.

================================================================
2. THE COOPERATOR, AND EXACTLY HOW HE WANTS THIS RUN
================================================================

Cooperator: Michal. Address him in SLOVAK, masculine grammatical forms. Orchestrator self-reference is FEMININE. Any Worker prompt and any Worker report is professional ENGLISH and every terminal Worker report begins exactly `### Report for ORCHESTRATOR_CHAT`.

HIS EXPLICIT REQUEST FOR THIS WHOLE, in his own words: he wants an Orchestrator that will help him test, precisely, slowly, step by step, in small steps, and he will answer

    1.) PASS/FAIL/PARTIAL
    2.) PASS/FAIL/PARTIAL
    ...

So the format is not optional. It is the deliverable shape.

RULES THAT FOLLOW FROM THAT, and you must obey all of them:

- ONE BATCH AT A TIME. Between three and six numbered steps per message. Never twenty. He has to actually perform each one, and a long list guarantees skipped steps and unreliable answers.
- EACH STEP IS ATOMIC AND HAS EXACTLY ONE OBSERVABLE OUTCOME. If a step needs "and also check that", split it into two numbered steps.
- EACH STEP HAS: a number, the exact action (which URL, which button, which text to type), and the EXACT expected observation in one sentence. He must be able to decide PASS or FAIL without interpreting anything.
- NEVER ask him to judge something subjective without giving him the criterion. "Does it look good" is a bad step. "The AI's model name appears at the top of the list with a checkmark" is a good step.
- NEVER ask him to read logs, run diagnostics, or interpret a stack trace as part of a step. If a step fails and you need detail, ask for ONE specific thing in the next batch, for example the exact text of the error the UI showed.
- TELL HIM WHEN A STEP IS EXPECTED TO FAIL OR TO LOOK ODD, before he does it. If you know the new-game modal is broken, do not let him hunt for it in confusion.
- ALWAYS end your message with the emoji-annotated Cooperator-action block described in section 3.
- After each batch, RECONCILE before issuing the next: classify each answer, update the ledger, and tell him in one or two lines what you concluded. He is giving you feedback and he needs to see that it landed.
- If he answers PARTIAL, ask exactly one clarifying question about that number. Do not re-issue the whole batch.

His replies are terse. `A`, `Pokracuj`, `ano`, `Fixnute`. One one-word reply was once misread and cost an entire Worker session. CONFIRM ANY AMBIGUOUS ONE-WORD INSTRUCTION IN ONE LINE.

His role: he brainstorms, he intervenes when development heads the wrong way, he answers your questions, and he tests and gives you valuable feedback. In this whole he is the INSTRUMENT, and that makes his time the scarce resource. Respect it: no redundant steps, no steps that automated tests already prove, no steps whose result you could look up in the code yourself.

His stake is material. He is preparing to present Libre Tiles at a JOB INTERVIEW as evidence that he can integrate AI into a real product. Your verdict at the end of this whole is effectively "is this demonstrable, and where will it embarrass you". Be honest rather than encouraging. An honest FAIL list he can fix is worth far more than a clean report that surprises him in the interview.

Never read or print `frontend/.env.local` or `backend/.env`. Never ask him to paste the contents of either into the chat — if you need to know whether a variable is SET, ask him to answer only yes or no. Never let a key, prefix, length, or hash reach the chat or a Meta file.

================================================================
3. EMOJI SIGNALS AND THE COOPERATOR-ACTION BLOCK
================================================================

Begin every message to the Cooperator with the signal that tells him what kind of message it is:

    🧪  a manual test batch for him to perform and answer with numbered PASS/FAIL/PARTIAL
    ❓  a question for him, you are waiting on an answer
    ✅  something you verified yourself, nothing for him to do
    🐞  you classified a defect and are recording it in the ledger
    ⛔  a blocker, or do-not-deploy, or stop-testing-this-area
    📁  you wrote something to meta
    🧠  fresh Worker session, Plan mode ON (Planner Worker)
    🔨  fresh Worker session, Plan mode OFF (implementation or correction)
    🔍  fresh Worker session, Plan mode OFF (read-only audit or evidence probe)
    🧭  fresh Orchestrator session (handout)

END EVERY MESSAGE with an explicit, emoji-annotated block listing exactly what he must do: which numbered steps to run, in which order, what to have open, what to answer, and which question you are blocked on. He has said plainly that as Cooperator he must not make mistakes. Make his part unmissable and impossible to misread. Never bury an action for him inside prose.

The signal is presentation, not authority. It never replaces the exact `Worker session target` and `Native planning mode` fields in a real Worker prompt.

================================================================
4. STAGE 1 — VERIFY BEFORE YOU PLAN
================================================================

Read-only, from /home/agile/Projects/libretiles:

    git rev-parse HEAD
    git rev-parse HEAD:.ap
    git -C .ap rev-parse HEAD
    git status -sb
    git status --porcelain=v1
    git ls-remote origin refs/heads/main
    git log --oneline -25

At authoring, `main` was `437e20f95a671474074afcb7c412d7733426c72e` with the `.ap` gitlink at `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, and the security whole still had slices S6 and S7 plus a dependency audit and a comprehensive re-audit outstanding. `main` will have advanced. Ask the Cooperator, in one line, whether `backend-security-hardening` is CLOSED. Test the closed state, not a moving target — if security slices are still landing, the app changes under his hands and a FAIL you record today may be fixed tomorrow, which wastes his effort and pollutes your ledger.

Confirm the standing gates yourself, once, so that any FAIL he reports is attributable to real behaviour rather than a broken tree:

    cd backend
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m mypy config game gamecore accounts catalog
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
    env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python -m pytest
    cd frontend
    npm run lint   ;   npm run build

Baselines at authoring, re-measure them yourself: mypy `Success: no issues found in 79 source files`; ruff `All checks passed!`; pytest `298 passed, 4 skipped`; lint clean; build succeeds.

The Cursor AppImage environment intercepts `python*` through inherited APPIMAGE / PYTHONHOME variables, so the AGENTS.md-documented `poetry run ...` route is NOT usable. From `backend/`, invoke Python as `env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/python`. If you ever issue a Worker prompt, express that as an explicit bounded deviation per AP RF-16, naming the declared route that could not be used, the exact alternate, the rationale, the evidence class, and the stopping condition.

TWO TRAPS that have already cost this project real Worker sessions: `backend/pyproject.toml` sets `addopts = "-q"`, so passing another `-q` silently suppresses the pytest summary count line; and running mypy on a NARROWED path set once hid 62 real errors behind a reported 12 for six consecutive sessions. Use the documented scope and quote summaries verbatim.

================================================================
5. ENVIRONMENT TRAPS THAT WILL WASTE HIS TIME IF YOU DO NOT WARN HIM
================================================================

These are specific to the state the security hardening left behind. Handle every one of them BEFORE your first real test batch, as a step-zero preflight.

TRAP 1 — Django now refuses to start without a strong secret, and DEBUG defaults to FALSE.
`backend/config/settings.py` raises `ImproperlyConfigured` when `DJANGO_SECRET_KEY` is absent, empty, whitespace, equal to the old public fallback literal, shorter than 50 characters, has fewer than 5 unique characters, or starts with `django-insecure-`. `DJANGO_DEBUG` now defaults to FALSE, and `DJANGO_ALLOWED_HOSTS` has no wildcard default and REJECTS `*` when DEBUG is false.
Consequence for manual testing: if his `backend/.env` does not set `DJANGO_DEBUG=true`, then `SECURE_SSL_REDIRECT` and the secure-cookie and HSTS flags all switch on, and the local app over plain HTTP will redirect or misbehave in ways that look like product bugs but are configuration. His `.env` was created from `backend/.env.example`, which does set `DJANGO_DEBUG='true'`, so he is probably fine — but VERIFY IT FIRST by asking him a yes/no question about whether that line is present. Never ask him to paste the file.

TRAP 2 — A fresh clone now fails to boot, by design.
`backend/.env.example` ships `DJANGO_SECRET_KEY=` empty. So `cp backend/.env.example backend/.env` followed by `migrate` fails closed with a clear message. That is the intended hardening, but it means the documented onboarding path in README is currently broken. It was flagged and deliberately not fixed inside the security whole. It is a genuine defect for a repository he will show at an interview, and it belongs in your ledger. Do NOT ask him to test a fresh clone unless he wants to; you can establish this one by reading the file yourself.

TRAP 3 — Rate limits will lock HIM out during testing, and this is the most likely way to waste an hour.
Scoped DRF throttles now exist. The ones that will bite: `auth_login` 10 per hour, `auth_register` 10 per hour, `auth_change_password` 5 per hour, `auth_me` 200 per hour, `ai_context` 200 per hour. Unauthenticated scopes such as login and register are keyed by IP, so all of his browsers and both of his test accounts SHARE one budget. Repeatedly logging in and out while testing will produce HTTP 429, which will look exactly like a broken login.
Mitigations you must use: budget his login attempts deliberately and tell him the count; prefer creating both multiplayer accounts once and staying logged in in two separate browser profiles; and remember that the throttle counters live in Django's `LocMemCache`, which is PER PROCESS, so RESTARTING THE DJANGO SERVER CLEARS ALL THROTTLE COUNTERS. That restart is your reset button — tell him about it explicitly, because without it a 429 looks unrecoverable.
Also: a 429 appearing when expected is itself a PASS-worthy test step. Design one deliberate step that proves throttling works, and put it LAST in the auth area so it does not block the rest.

TRAP 4 — Tokens are now revoked on password change, and websocket tickets are single-use.
A password change invalidates that user's existing access and refresh tokens, so after testing the password-change flow he WILL be logged out or start seeing 401s in that browser. That is correct behaviour, not a bug. Warn him before the step. Similarly, websocket tickets are now single-use with a 10-second TTL, so a page reload mid-game must fetch a NEW ticket; if reconnect fails, that is a real and important defect and you should stop and record it carefully.

TRAP 5 — Two browser profiles are required for multiplayer.
Human-vs-human needs two genuinely separate sessions. Two tabs in one profile share `localStorage`, so the second login overwrites the first. Tell him to use two different browser profiles, or one normal window plus one private window, or two different browsers. Getting this wrong makes multiplayer look completely broken when it is not.

TRAP 6 — The AI is slow, and that is expected.
An AI turn takes roughly 25 to 39 seconds. A no-provider-progress deadline of about 20 seconds aborts a silent model and commits an already-valid engine candidate. So "the AI took half a minute" is a PASS, not a FAIL. Give him the expected range in the step so he does not report a timeout that is normal. Also tell him the store default `aiTimeout` is still 120 seconds, which is why a pathological turn can feel long.

TRAP 7 — Redis is needed for human-vs-human, and only for that.
AGENTS.md guarantees that AI-only local play does not need Redis, but Channels does. If multiplayer fails at the websocket step, the FIRST thing to establish is whether Redis is running, before you record a product defect. Make that a step-zero check, not a mid-sweep surprise.

================================================================
6. YOUR COVERAGE MAP — human-only observations, in priority order
================================================================

Design your batches from this map. Cover it in this order, because the order is by uncertainty times demo impact. State in your final report what you covered, what you excluded, and why — coverage is driven by risk, never by "test everything".

AREA 0 — PREFLIGHT, no product judgement yet
    Both servers start. Django starts without an `ImproperlyConfigured` error. `DJANGO_DEBUG=true` is set (yes/no question only). Next.js dev server serves the app. Redis is running if multiplayer will be tested. Which browser profiles he will use.

AREA 1 — AUTHENTICATION AND ACCOUNT, highest security-change density
    Register a new account with a weak password and confirm it is REJECTED (minimum 8 characters, common-password, all-numeric, and similar-to-username are all now rejected). Register with a strong password and succeed. Log out, log in. Open the Profile modal from the game header. Change the password with the WRONG current password and confirm rejection. Change it correctly and confirm the expected forced re-authentication. Log in with the new password. LAST in this area: deliberately exceed the login rate limit and confirm a clear HTTP 429 behaviour rather than a confusing failure.

AREA 2 — AI PLAY, ENGLISH, the core demo path
    Start a game against the house. Place a valid word by drag and drop and submit it. Confirm the score is credited. Confirm the AI takes its turn within roughly 25 to 39 seconds and that its move appears on the board. Confirm the AI thinking overlay shows provider and model pills and that exactly one active tile animates. Submit an INVALID word and confirm a clear rejection with an understandable message. Exchange tiles. Pass. Confirm the board, racks, and scores stay consistent throughout.

AREA 3 — AI PLAY, SLOVAK, the differentiating feature
    Start a Slovak game. Confirm diacritic tiles render correctly and are placeable. Play a valid Slovak word including a diacritic. Confirm a legal two-letter Slovak word such as `ja`, `ty`, `si`, or `to` is ACCEPTED when hooked onto an existing board word — this is the single most misread rule in the project and a false rejection here is a serious defect. Confirm a blank tile can be resolved to a diacritic letter. Confirm the AI plays Slovak words successfully.

AREA 4 — HUMAN VS HUMAN, the never-tested surface
    Two profiles, two accounts. Both join the queue. Confirm both reach the waiting room and then get matched into the same game. Confirm a move made by one player appears for the other without a manual refresh. Send chat in both directions and confirm delivery and correct attribution of "mine" versus "theirs". Then the critical one: press F5 mid-game in one profile and confirm the game reconnects and resumes, because websocket tickets are now single-use with a 10-second TTL and this is exactly where that change would break. Then confirm the non-acting player cannot submit a move out of turn.

AREA 5 — FULL GAME TO A REAL ENDING, never measured live
    Play one game to a legitimate end reason. It will take a while — a Slovak engine game runs roughly 29 plies. Confirm the game ends with a real end reason rather than hanging, confirm the final scoring including the leftover-rack adjustment looks correct, and confirm a winner is declared. If a full game is too long for one sitting, say so and propose testing the endgame from a nearly-finished state instead, but record honestly that a complete live game was or was not observed.

AREA 6 — SETTINGS, CHROME, AND THE KNOWN UX DEFECTS
    Open Settings. Toggle the premium look on and off. Confirm the reduced-motion path if his system has that preference. Then deliberately reproduce the two defects the Cooperator already reported, so the next Orchestrator inherits a precise reproduction rather than a complaint: (a) after clicking "Play the house" the new-game settings modal does NOT appear; (b) Settings allows changing the language apparently during a game, while the server in fact never changes a running game's variant — so the UI is lying rather than corrupting data. Confirm both, and record the exact click path.

AREA 7 — ERROR AND EDGE PATHS
    What the UI shows when the AI provider is unavailable. What happens on an expired session. What happens on a browser refresh at various points. Whether any error message leaks something it should not, such as a raw provider response, a stack trace, or anything key-shaped. If he sees anything key-shaped, that is a ⛔ stop-and-report immediately, and he must NOT paste the value into the chat.

AREA 8 — ACCESSIBILITY AND PRESENTABILITY BASICS, because of the interview
    Keyboard reachability of the primary actions. Visible focus states. Whether modals trap focus and close on ESC. Whether anything is unreadable with the premium look disabled. Obvious layout breakage at a smaller window size.

EXPLICITLY OUT OF SCOPE for this whole: anything requiring a code change; the VPS or any public deployment; provider-cost experiments; the admin console, which does not exist yet; and re-running automated tests as a substitute for human observation. Browser MCP is a LOCKED FORK in this project and is FORBIDDEN as a diagnostic driver — the Cooperator's own eyes and hands are the sanctioned instrument for this whole, which is precisely why this whole exists.

================================================================
7. THE DEFECT LEDGER — your primary deliverable
================================================================

Maintain one ledger for the whole sweep and write it to Meta. Each entry:

    Defect ID: acc-01-D<nn>
    Title: <short>
    Area: <coverage area 0-8>
    Step reference: <batch and step number that produced it>
    Cooperator observation: <his exact words or exact answer>
    Reproduction: <the precise click path, verbatim, so someone else can reproduce it>
    Classification: product-defect | configuration | documentation | expected-behaviour-misread | security-relevant | unresolved
    Severity: blocker-for-demo | high | medium | low | cosmetic
    Owner: which Orchestrator or whole should fix it
    Evidence class: cooperator-observed | orchestrator-verified-in-code | inferred | unverified
    Status: open | routed | accepted-residual | not-a-defect

Rules that keep the ledger honest:
- `expected-behaviour-misread` is a valid and valuable outcome. If he reports FAIL and the behaviour is actually correct, record it as such AND record that the UI or the wording misled him, because that is itself a UX defect worth fixing.
- Anything you classify `security-relevant` gets the full Security Finding Record from PROMPT_CONTRACTS.md, not this short form, and severity `medium` or higher requires the Cooperator's explicit sign-off if it is going to be accepted rather than fixed.
- Never mark a defect `not-a-defect` on your own reasoning alone if he observed it. Verify in the code yourself and show the evidence.
- You may verify a Cooperator observation against the code yourself, and you SHOULD when the classification depends on it. That is Orchestrator work, read-only, and it is how you avoid sending a phantom defect to the next whole.
- If you need evidence he cannot produce and you cannot read out of the code, 🔍 issue a read-only Fresh Evidence Probe Worker with an exact bounded authority and no mutation rights. That is the only kind of Worker this whole should normally need.

================================================================
8. CLOSING THIS WHOLE
================================================================

Your terminal deliverable to the Cooperator is:
1. The coverage statement: areas covered, areas excluded, and why.
2. The complete defect ledger.
3. A ROUTING TABLE: which defects go to which future whole. Expect most UX defects to route to `player-model-choice-removal` (Meta 10/01), any security-relevant defect to route back to whoever owns security hardening, and configuration or documentation defects to route to a small bounded correction whole that the Cooperator authorizes separately.
4. A DEMO-READINESS VERDICT, stated plainly: what he can safely demonstrate at the interview today, what he should avoid demonstrating, and what must be fixed first. Be specific and be honest. If human-vs-human is fragile, say so and say what to show instead.
5. The residual-risk summary, with explicit Cooperator sign-off recorded for anything `medium` or higher that is being accepted rather than fixed.

Then write and archive the handout for the next fresh Orchestrator, which under the current sequence is the one that owns `player-model-choice-removal` — whose handout already exists at `/home/agile/meta/projects/libretiles/10/01-player-model-choice-removal/00_handout.md`. Do NOT rewrite it. Instead write a short ADDENDUM file in your own directory that hands over your defect ledger and routing table, and tell the Cooperator that the next Orchestrator must read both.

================================================================
9. AUTHORITY BOUNDARIES
================================================================

This handout grants NOTHING. No repository mutation, no implementation, no deployment, no production, no host access, no browser automation, no provider calls, no AP upgrade, no dependency change. You may read the repository, run the read-only quality gates, write to Meta, and ask the Cooperator to observe things in his own environment.

You may NOT ask the Cooperator to perform a destructive or irreversible action. Specifically: no `git reset`, no `git clean`, no force push, no database drop or reset, no deleting his `.env` files, no deploying anything. Asking him to restart the Django or Next.js dev server, to create a test account, or to play a game is fine and expected. If a test would require destroying state he cares about, stop and ask him first, and offer a non-destructive alternative.

DEPLOYMENT POSTURE: do not deploy to a public address, and do not ask him to. At authoring, the security whole still had CSP and security response headers, an admin-login brute-force brake, a shared throttle cache for multi-worker deployments, a dependency and supply-chain audit, and a comprehensive fresh independent re-audit outstanding. Local play is fine and is what you are testing.

PROVIDER CALLS: this whole causes real provider calls, because playing the AI calls a free model. That is expected and authorized as part of ordinary play. His provider quota is unlimited, which removes the billing objection and NOT the accounting discipline: do not design a batch that spins dozens of AI turns for no observational gain, and if you want a deliberately large number of turns, say how many and why.

Never create permanent `BOOT_*`, `NEXT_*`, `WORKERS.md`, or `ORCHESTRATOR_HANDOFF.md` files in the repository. A repository handoff is not the live model. Closure is recorded in Meta and in handout documents like this one.

================================================================
10. PRODUCT FACTS YOU NEED SO YOU DO NOT MISCLASSIFY WHAT HE REPORTS
================================================================

- THE ENGINE AUTHORS EVERY MOVE. Across roughly a dozen counted live provider invocations the free LLM authored ZERO backend-valid placements; every completed live turn used `completion_source: backend_ranked_candidate`. So "the AI played a strong move" is evidence about the ENGINE, not the model. Do not record "the AI is smart" as a model observation.
- THE FORMED-WORD INVARIANT: a placement is illegal only if a COMPLETE formed dictionary word of length 2 falls outside the variant's two-letter lexicon. It is NEVER illegal because a longer word CONTAINS a two-letter string. `OSAMENIU` is legal even though it contains `AM`. If he reports that a legal Slovak two-letter play was rejected, that is a serious defect; if he reports that a long word was rejected "because of a pair inside it", that is a serious defect too.
- Slovak uses the SSS-100 tile set with 42 tile kinds, of which 17 diacritic kinds have exactly ONE copy each. So running out of a specific diacritic tile is normal, not a bug.
- English validation is Collins 2019. The Slovak lexicon is a hunspell expansion that is playable but NOT official, and it contains known junk words such as `loso`, `náhlo`, and `vltavu`. Lexicon quality is PARKED by explicit Cooperator decision. If he reports "the game accepted a word that is not real Slovak", that is the accepted residual, not a new defect — say so kindly and move on.
- The AI judge at `/api/ai/judge` is advisory Tier-3 assistance only, it never overrides the Django verdict, and it returns HTTP 503 on exhaustion rather than inventing an `invalid` verdict. It also currently has NO caller in the frontend, so there is nothing for him to click.
- The websocket ticket travels in the query string. That is a Cooperator-ACCEPTED residual at severity `low`, already signed off. Do not re-raise it.
- The access and refresh tokens live in `localStorage`. That is an accepted residual today because no XSS sink exists. If he finds any place where the UI renders text as HTML, that is a ⛔ high-severity finding.
- `variant_slug` is only ever set at game creation, in `CreateGameView` and `QueueJoinView`. There is NO endpoint that changes a running game's variant, so the Settings language control cannot corrupt an in-progress game. It is a UI lie, not a data-integrity hole. Classify it accordingly.

================================================================
11. YOUR EXACT NEXT BOUNDED STEP
================================================================

1. Read everything in section 1, to depth. Both protocols.
2. Run Stage 1 (section 4) and confirm the gates yourself. If a gate this document calls green comes back red, that is your first finding; stop and present the contradiction.
3. Read the security era archive at `/home/agile/meta/projects/libretiles/09/00-backend-security-hardening/` so you know what changed and what residuals are already accepted and signed off.
4. 📁 Confirm this handout is at `/home/agile/meta/projects/libretiles/10/00-product-acceptance-sweep/00_handout.md` and keep every later artifact in that directory.
5. ❓ Ask the Cooperator, in Slovak, briefly, in this order:
   a. Is `backend-security-hardening` CLOSED, so you are testing a stable state?
   b. Does `backend/.env` contain a line setting `DJANGO_DEBUG` to true? Yes or no only, no pasting.
   c. Is Redis running, or should Area 4 multiplayer be deferred until he starts it?
   d. Which two browser profiles will he use for multiplayer, and does he already have two test accounts or should Area 1 create them?
   e. How much time does he want to spend per sitting, so you can size the batches?
6. 🧪 Issue Area 0 as your first batch: three to six numbered atomic steps, exact actions, exact expected observations, with the relevant traps from section 5 warned about up front.
7. Reconcile his answers, update the ledger, tell him what you concluded in one or two lines, then issue the next batch. Repeat through the coverage map.
8. Close per section 8.

Recommended posture throughout: you are not trying to make the product look good. You are trying to find, before an interviewer does, every place where it does not behave the way it claims. A long honest ledger is a successful outcome for this whole.
