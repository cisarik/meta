# Libre Tiles MVP: päť bezplatných AI providerov, úplné partie a cesta k silnému Scrabble súperovi

## 1. Cieľ a uzamknuté rozhodnutia

Východiskom je lokálny commit `8603459edab8f8be9a26c9db88b5b490d5694a79`, ktorý už opravuje fallback po chybe „No endpoints found“. Tento commit zostáva zachovaný a jeho regresné testy sa nesmú oslabiť.

MVP má tri postupné brány:

- **T0 – transport:** provider vie vykonať presný `validateMove → tool result → finishMove` ping-pong.
- **T1 – legálny ťah:** každý AI turn skončí jedným serverom potvrdeným ťahom alebo čistým vyčerpaním providerov bez zmeny hry.
- **T2 – úplná hra:** AI a deterministický súper dohrajú partiu podľa pravidiel, bez slučky, straty kameňov alebo nesprávneho skóre.

Priama fallback priorita bude:

1. Groq
2. Google Gemini
3. Cloudflare Workers AI
4. Mistral
5. IBM watsonx.ai

Aion a Hugging Face sa pripravia ako neaktívny watchlist. NVIDIA NIM a OpenRouter ostanú ako kompatibilný chvost a explicitná stará používateľská preferencia, ale nebudú predvolenou cestou.

Nové riadky providerov vzniknú s `is_active=false`. Provider sa zobrazí v hre až po:

1. nakonfigurovaní serverových credentials,
2. úspešnom capability probe,
3. explicitnej aktivácii operátorom v Django Admin.

Priamy platený OpenAI provider sa nepridá, pretože nespĺňa požiadavku opakovane bezplatného API. Implementuje sa však všeobecný OpenAI-compatible transport a Groq bude hostiť OpenAI open-weight model `openai/gpt-oss-120b`; GPT-OSS nie je poskytovaný cez OpenAI API ani ChatGPT. [OpenAI GPT-OSS FAQ](https://help.openai.com/en/articles/11870455)

Prompt sa pred prvým stabilným benchmarkom nebude meniť. Najprv sa oddelí transportná spoľahlivosť od kvality promptu; následne sa zmeria pôvodný prompt a až potom vznikne verzovaný strategický prompt.

## 2. Provider a runtime architektúra

### Presné páry

| Provider | Model | Serverová konfigurácia | Overený bezplatný rámec |
|---|---|---|---|
| `groq` | `openai/gpt-oss-120b` | `GROQ_API_KEY`, `https://api.groq.com/openai/v1` | Free plán; dokumentované tool calling a limity 30 RPM, 1 000 RPD, 8k TPM, 200k TPD. [Groq limits](https://console.groq.com/docs/rate-limits), [tool calling](https://console.groq.com/docs/tool-use/local-tool-calling) |
| `google-gemini` | `gemini-3.7-flash` | `GEMINI_API_KEY`, `https://generativelanguage.googleapis.com/v1beta/openai` | Free vstup/výstup podľa modelu a projektových kvót; OpenAI shim je beta, preto je named-tool probe povinný. [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai) |
| `cloudflare-workers-ai` | `@cf/zai-org/glm-4.7-flash` | `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | 10 000 Neurons/deň; GLM Flash ostáva vo free kohorte. [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), [model](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) |
| `mistral` | `mistral-small-2603` | `MISTRAL_API_KEY`, `https://api.mistral.ai/v1` | Mistral Free Mode; použiť pripnuté ID, nikdy `latest`. [Free Mode](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key), [chat API](https://docs.mistral.ai/api/endpoint/chat) |
| `ibm-watsonx` | `ibm/granite-4-h-small` | `IBM_CLOUD_API_KEY`, `IBM_WATSONX_PROJECT_ID`, `IBM_WATSONX_REGION` | Lite limit 300k tokenov/mesiac. IAM token sa získava samostatne. [IAM API](https://cloud.ibm.com/docs/apis/iam-identity-token-api), [watsonx API](https://cloud.ibm.com/docs/apis/watsonx-ai) |

Watchlist:

- `aion` / `aion-labs/aion-3.0-mini` / `AION_API_KEY`
- `huggingface` / `openai/gpt-oss-120b:groq` / `HF_TOKEN`

Presné modelové ID sa nesmie potichu nahradiť. Ak provider model vyradí, nový pár vyžaduje nové oficiálne overenie a Orchestrator-authorized zmenu.

### Verejné a serverové rozhrania

Frontend dostane client-safe registry presných párov, názvov a kanonického poradia. Secrets ani base URL nebudú súčasťou client bundle.

Serverový runtime kontrakt bude asynchrónny kvôli IBM IAM:

```ts
getLanguageRuntime(
  provider: string,
  modelId: string,
): Promise<{
  model: LanguageModel;
  tracker: ProviderRequestTracker;
}>
```

`ProviderRequestTracker` bude zaznamenávať:

- skutočný počet modelových aj IAM HTTP požiadaviek,
- normalizované token usage,
- voliteľné sanitizované `retry_after_seconds`,
- žiadne raw hlavičky, request body, odpovede, reasoning ani credentials.

Groq, Gemini, Cloudflare, Mistral, NIM, OpenRouter, Aion a Hugging Face použijú existujúci `@ai-sdk/openai`. IBM dostane samostatný adaptér:

- region iba z allowlistu `eu-de`, `eu-gb`, `us-south`, `jp-tok`, `au-syd`,
- IAM token cache s jedným súbežným refreshom a obnovou 60 sekúnd pred expiráciou,
- inference endpoint `/ml/v1/text/chat?version=2023-10-25`,
- mapovanie `model ↔ model_id` a doplnenie `project_id`.

Chýbajúca alebo placeholder credential skončí `provider_auth_failed` ešte pred sieťovým volaním. Neznámy provider, nesprávna kombinácia provider/model, svojvoľný model alebo base URL z prostredia zlyhá uzavreto.

Prvý krok ostane named `validateMove`. Cloudflare adaptér smie preložiť named tool choice na `"required"` iba vtedy, keď je aktívny práve jeden nástroj – `validateMove`. Pri dvoch nástrojoch nesmie meniť význam requestu.

### Fallback a rozpočty

- `MAX_FALLBACK_ATTEMPTS = 5`.
- Platná používateľská preferencia je prvá; zvyšok zachová kanonické poradie bez duplicít.
- Nový používateľ dostane prvý aktívny riadok, teda Groq po jeho aktivácii.
- Predvolený nový účet: 120 sekúnd a 50 provider krokov. Existujúce uložené nastavenia sa neprepíšu.
- Judge: najviac päť pokusov, 10 sekúnd na provider, 50 sekúnd celkovo.
- AI SDK `maxRetries: 0`; pri 429, auth chybe, timeoutoch, unsupported tools, nedostupnom modeli alebo „No endpoints found“ sa okamžite pokračuje ďalším providerom.
- Fallback pokračuje iba po potvrdení, že backendový turn ostal nezmenený.

Čas jedného pokusu:

```text
min(remainingSeconds, max(15, floor(remainingSeconds / attemptsLeft)))
```

Provider kroky musia rezervovať minimálne päť krokov pre každý neskorší lane:

```text
attemptStepGrant =
  max(5, remainingSteps - 5 * (attemptsLeft - 1))
```

Neúspešný lane odpočíta najmenej päť krokov alebo skutočný vyšší počet requestov. Tým prvý pomalý provider nemôže spotrebovať celý turn.

### Pravidlá hry a API

Libre Tiles prejde na WESPA ukončenie po šiestich po sebe idúcich bezbodových ťahoch. Pass aj exchange sa počítajú ako bezbodový ťah; úspešné položenie resetuje počítadlo. [WESPA Rules](https://www.wespa.org/features/rulesv1.pdf)

- `consecutive_passes` sa dátovou migráciou premenuje na `consecutive_scoreless_turns` so zachovaním hodnoty.
- `pass_streak` prestane rozhodovať o konci hry a bude znamenať iba skutočné po sebe idúce passy.
- Nový dôvod konca: `SIX_CONSECUTIVE_ZERO_SCORES`.
- Remíza bude mať `winner_slot=null` a API/history výsledok `draw`; nesmie sa zobrazovať ako abandoned.
- Bežný koniec po vyprázdnení racku a bagu ostáva nezmenený.

## 3. AP implementačný program a Worker prompty

Každý rez vykoná nový Worker nad prijatým commitom predchodcu. Prvý implementačný Worker použije session ordinal 14; ďalšie 15–21. Ak sa AP ledger pred začiatkom zmení, Orchestrator mechanicky použije najbližšie voľné monotónne číslo.

Každý implementačný prompt dostane tento záväzný obal:

```text
Logical whole identity: playable-free-rivals
Worker session ordinal: <assigned ordinal>
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Task phase: Implementation
Implementation authority: explicit
Exact baseline: <accepted predecessor SHA>
Changed-path allowlist: <paths from the assigned slice>
Implementation boundaries: implement only the positive scope below; all listed
negative scope is forbidden
Independence required: no

Before changes, read completely:
- AGENTS.md
- .ap/AP.md
- .ap/AP_WORKER.md
- .ap/PROMPT_CONTRACTS.md
- .ap/PROMPT_ENGINEERING_PATTERNS.md when the slice touches prompts

Re-gate HEAD, clean status, .ap gitlink and `./.ap/ap doctor`.
Treat .ap/ as read-only.
Use apply_patch for edits.
Do not use real credentials, provider network calls, push, deploy, account
changes, Admin activation, or unrelated cleanup.
Run focused tests first and the declared full gates afterward.
If all gates pass, create exactly one local commit with the prescribed message.
Never push.

Report with heading exactly:
### Report for ORCHESTRATOR_CHAT

Include baseline, resulting commit, changed files, test evidence, residual risks,
phase result implementation-PASS|implementation-FAIL, and closure not-closed.
```

### Worker 14 — katalóg providerov

- Baseline: `8603459edab8f8be9a26c9db88b5b490d5694a79`.
- Allowlist: `backend/catalog/selection.py`, `seed_models.py`, nová migrácia `0012_multi_provider_free_rivals.py` a nové katalógové testy.
- Implementovať priame poradie top päť, watchlist a kompatibilný NIM/OpenRouter chvost.
- Nové riadky vytvoriť neaktívne; seed ani migrácia nikdy nesmú prepnúť `is_active` existujúceho riadku.
- Reverse migrácia nové presné páry iba deaktivuje, nemaže ich.
- Dynamic flag ovplyvní iba OpenRouter chvost.
- Commit: `feat(catalog): prepare direct free rivals`.

### Worker 15 — štandardné OpenAI-compatible runtime adaptéry

- Baseline: prijatý commit Workera 14.
- Allowlist: frontend registry/model-catalog/runtime moduly a testy, OpenRouter/NIM klienti, Move/Judge route nutné pre async factory, `.env.local.example`.
- Implementovať registry, exact-pair validáciu, tracker a Groq/Gemini/Cloudflare/Mistral; Aion/HF iba ako neaktívne deskriptory.
- Zachovať NIM/OpenRouter kompatibilitu a existujúcu 404 regresiu.
- Žiadna nová AI SDK závislosť.
- Commit: `feat(ai): add direct free provider runtimes`.

### Worker 16 — IBM watsonx runtime

- Baseline: prijatý commit Workera 15.
- Allowlist: nový IBM adaptér a jeho testy, runtime registry/factory a env template.
- Implementovať region validáciu, IAM singleflight cache, skorý refresh, 401 refresh-once, request/response transform a spoločné accounting.
- Zakázať ľubovoľný host/region a raw logging.
- Commit: `feat(ai): add watsonx rival runtime`.

### Worker 17 — nezávislá runtime acceptance

Fresh read-only Acceptance Worker:

- nesmie nič opravovať ani commitovať,
- preverí exact-pair fail-closed správanie, nulový fetch bez credential, Cloudflare transform, IBM cache/refresh, sanitizáciu a Move/Judge kompiláciu,
- spustí všetky frontend testy, lint, TypeScript a build,
- pri zlyhaní Orchestrator zadá samostatnému Correction Workerovi iba konkrétny defect a potom zopakuje fresh acceptance.

### Worker 18 — päť-lane orchestration

- Baseline: prijatý runtime acceptance commit.
- Allowlist: fallback, Move/Judge routes a testy, SSE tracker, Zustand AI nastavenia, Settings a attempt overlay.
- Implementovať cap päť, časové segmenty, rezerváciu krokov, 120/50 defaults, Judge 5×10/50, `retry_after_seconds` a piate úspešné fallback rameno.
- Overlay zobrazí všetkých päť pokusov a iba jeden aktívny ping-pong indikátor.
- Commit: `feat(ai): orchestrate five free rivals`.

### Worker 19 — WESPA koniec, remízy a full-game harness

- Baseline: prijatý commit Workera 18.
- Allowlist: Django game model/services/serializer, nová game migrácia, game testy, frontend outcome typy a history panel.
- Implementovať šesť bezbodových ťahov, draw reprezentáciu, zachovanie starých dát a deterministický full-game simulator.
- Nezasahovať do Collins autority ani povoľovania strategického exchange.
- Commit: `fix(game): adopt WESPA scoreless ending`.

### Worker 20 — capability probe a prevádzková dokumentácia

- Baseline: prijatý commit Workera 19.
- Allowlist: nový provider capability modul, unit/live Vitest súbory, `frontend/package.json`, env template, README a AI architektúra.
- Pridať explicitný `npm run probe:provider` test, ktorý je v bežnom test suite vždy skipnutý a nikdy sa nespustí pri boote, katalógu ani hre.
- Probe používa rovnaký `generateText` runtime ako produkcia, nie provider streaming.
- Commit: `test(ai): add provider capability probes`.

Probe kontrakt:

1. Vygenerovať náhodný nonce.
2. Vynútiť `validateMove` s presnými placements slova `RETAINS` cez stred:
   `(7,4,R)…(7,10,S)`.
3. Lokálny tool vráti `valid:true` a nonce ako pong.
4. Model musí po tool resulte zavolať `finishMove({ready:true})`.
5. Najviac tri modelové requesty; prose-only, chybný nástroj, zlá schéma alebo chýbajúce pokračovanie znamenajú FAIL.
6. Výstup obsahuje iba provider, model, status, latency a outbound count.
7. Statusy: `pass`, `not_configured`, `auth_failed`, `rate_limited`, `model_unavailable`, `named_tool_unsupported`, `tool_continuation_failed`, `schema_failed`, `timeout`, `unknown`.
8. Voliteľný provider-streaming diagnostický test sa môže zaznamenať, ale neblokuje aktiváciu, pretože produkčná cesta používa `generateText`.

### Worker 21 — finálna nezávislá acceptance

Fresh read-only Worker overí celý prijatý reťazec. Nemá correction authority. Pri chybe vznikne jeden úzko ohraničený Correction Worker a po ňom nová fresh acceptance. Push, deploy a živé credentials zostávajú samostatnou autoritou.

## 4. Testy a akceptačné brány

### Statické a syntetické testy

Backend:

- forward/reverse migrácie a zachovanie hodnôt,
- idempotentný seed a zachovanie Admin kill switchu,
- presné poradie pri dynamic flag off/on,
- OpenRouter sync nesmie meniť priame riadky,
- pass/exchange kombinácie: žiadny koniec po štyroch alebo piatich, koniec presne po šiestich,
- scoring move resetuje počítadlo,
- remíza, rack-empty koniec, finálne rack penalties,
- presne 100 kameňov vrátane blankov počas celej partie,
- `ruff`, plný `pytest`; mypy nesmie pridať chyby k známemu baseline 63 chýb v 17 súboroch.

Frontend:

- každý presný pár a odmietnutie provider/model spoofingu,
- adapter body/header transformácie bez odhalenia secretov,
- missing/placeholder env vykoná nula fetchov,
- IBM token cache, expirácia, singleflight a 401,
- cap päť, časový aj step budget, úspech až na piatom lane,
- Play/Judge používajú rovnakú queue,
- zachovanie unchanged-turn retry a „No endpoints found“ testu,
- kompletný Vitest suite najmenej na súčasnej úrovni 138 testov, ESLint, `tsc --noEmit`, production build.

### T1 – legálnosť každého turnu

Na deterministických aj mocked-provider scenároch:

- 100 % turnov skončí jedným legálnym terminalom alebo sanitizovaným provider exhaustion,
- nula duplicitných či nelegálnych persistovaných ťahov,
- pass/exchange sú zakázané pri `found`,
- pri `indeterminate` sa stav nemení,
- backend witness rescue sa vždy opätovne validuje,
- voľný text modelu nikdy nerozhoduje o place/pass/exchange.

### T2 – úplné partie

- Rýchly CI harness: 20 deterministických bag seedov, maximálne 200 plies.
- Pomalá acceptance: 100 seedov, maximálne 200 plies.
- Každá hra musí skončiť iba regulárnym rack-empty koncom alebo šiestimi scoreless turns.
- Po každom ťahu platí tile conservation, správny acting slot a prepočítané skóre.
- Žiadna opakovaná nezmenená pozícia ani nekonečný retry cyklus.
- Remíza musí zostať remízou cez Django API, frontend typy aj history UI.

### Živá acceptance po dodaní kľúčov

Živé volania sú samostatný explicitne autorizovaný krok:

- provider sa probuje samostatne a bez fallbacku,
- na hrateľný live MVP stačí aspoň jeden aktívny provider s PASS a jednou dokončenou hrou,
- tvrdenie „päť funkčných providerov“ je dovolené až po PASS všetkých piatich,
- dve počiatočné celé hry: seed A s AI ako prvým hráčom, seed B s obráteným starterom proti deterministickému legálnemu súperovi,
- neskôr jedna úplná hra pre každý aktívny provider.

Celý prvý live experiment sa zastaví pri prvom limite:

- 300 outbound requestov vrátane IBM IAM,
- 500k zaznamenaných tokenov,
- 50 % providerom publikovaného denného limitu,
- pre IBM navyše 150k tokenov, teda 50 % Lite mesačného limitu.

Ak provider neposkytne dôveryhodné usage údaje ani konzolovú kvótu, po capability probe sa jeho dlhší live test zastaví, kým sa nedá limit bezpečne merať.

## 5. Aktivácia, rollback a cesta k víťaziacej AI

### Rollout

1. Nasadiť kód a migrácie; nové riadky ostanú neaktívne.
2. Pridať serverové credentials bez commitu.
3. Overiť aktuálne free podmienky a spracovanie dát.
4. Spustiť capability probe jedného providera.
5. Pri PASS aktivovať presný riadok v Django Admin.
6. Spustiť jednu živú úplnú hru.
7. Opakovať podľa priority Groq → Gemini → Cloudflare → Mistral → IBM.

Rollback je deaktivácia konkrétneho riadku v Admin alebo revert izolovaného lokálneho commitu. Riadky ani históriu hier nemaže. OpenRouter/NIM kompatibilný chvost ostáva dostupný.

### Nasledujúca strength fáza

Po T2 sa zmrazí baseline provider/prompt/engine a až potom sa začne optimalizácia:

- Backend dostane samostatné ranked top-K vyhľadávanie; existujúci prvý witness ostane bezpečnostným API.
- Každý kandidát bude Collins-2019-validovaný a ohodnotený immediate score, rack leave, premiums, bingo potenciálom, board exposure a endgame hodnotou.
- Ak model top-K výber nedokončí, backend odohrá najvyššie hodnotený legálny kandidát.
- Prompt v2 dostane iba verejné údaje: premium políčka a ich použitie, bag count, počet kameňov súpera, verejnú tile históriu, score difference, game phase a scoreless-turn count. Nikdy neuvidí skrytý súperov rack.
- Strategický exchange bude povolený až vtedy, keď ho odporučí deterministický equity evaluator; samotný prompt ho nesmie autoritatívne zvoliť.
- Prompt migration bude SHA-256 hash-gated a nebude prepisovať Admin-customized prompty.

Strength acceptance:

- 120 pozícií: openings, hooks, parallels, premiums, blanks, rack leave, defense, bag phase a endgame.
- 100 % recall najlepšieho okamžitého skóre v top-K.
- Aspoň 95 % best-equity recall, median regret ≤2 body, p90 ≤8.
- Minimálne 100 seed-balanced hier proti dnešnému witness baseline, pozitívny priemerný spread a 95 % dolná hranica win-rate nad 50 %.
- Pre tvrdenie „poráža bežného domáceho hráča“ minimálne 100 dokončených vyvážených hier, pozorovaná bodová úspešnosť aspoň 60 % a Wilsonova 95 % dolná hranica nad 50 %.

Predvoleným produktovým cieľom MVP je teda spoľahlivo a legálne dohrať partiu. Cieľ víťaziť nad človekom sa dosiahne kombináciou exhaustívnejšieho Scrabble enginu, bezpečného top-K fallbacku, verejného strategického kontextu a meraného prompt engineeringu — nie samotnou výmenou LLM providera.
