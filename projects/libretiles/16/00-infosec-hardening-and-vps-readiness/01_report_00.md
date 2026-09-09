### Report for ORCHESTRATOR_CHAT

**IHR-SLICE-1-PLAN — podrobný implementačný plán INFOSEC hardeningu admin, simulation a auth rozhraní**

```text
Logical whole identity: infosec-hardening-and-vps-readiness
Worker session ordinal: 01
Worker exchange ordinal: 01

status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed

Start commit: a892f740f194af2492c3865a9a1ea6dcf18ed1a7
End commit: a892f740f194af2492c3865a9a1ea6dcf18ed1a7
AP pin: 9c5cc44f8b6c92dd56ad2427d13223d7d59c5656
Branch: main
Evidence tier: E0
Evidence posture: non-independent

Changed files and purpose: none
Commit/push result: not-applicable
Delivery: complete planning report in chat, explicitly accepted by Cooperator.
Meta report file: not written; archival is outside this revised delivery contract.
```

**Význam PASS:** plánovací výstup je dokončený a odovzdaný podľa upraveného kontraktu. PASS neznamená, že navrhované opravy už boli implementované, že aplikácia absolvovala nezávislý bezpečnostný audit alebo že je uzavretý celý logical whole.

```text
Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0
```

Predchádzajúce zastavenie sa týkalo nemožnosti zapísať report v Plan Mode. Cooperator následne výslovne prijal kompletný plán v chate ako finálne odovzdanie. Technický plán pred týmto reportom odovzdaný nebol.

**Zhrnutie výsledku**

Väčšina predpokladaných základných ochrán už existuje. Slice 1 preto nemá zavádzať nový systém administrátorských oprávnení. Potrebuje doplniť chýbajúce regresné testy a vykonať štyri ohraničené opravy:

1. Zabrániť tomu, aby dokončený refresh obnovil odhlásenú reláciu alebo prepísal novú identitu.
2. Zjednotiť spracovanie chybných a neexistujúcich identifikátorov simulácie na kontrolované 404.
3. Obmedziť voľné diagnostické JSON údaje vracané v replay a explicitne premietať verejnú konfiguráciu simulácie.
4. Obmedziť chybové payloady vracané cez Next.js simulation proxy a otestovať jej skutočné delegovanie LLM vetvy.

Zachovať existujúci spoločný `refreshPromise`, pravidlo GET-any-staff / mutate-creator-only, existujúcu autoritu Django a všetky prijaté rozhodnutia A1–A7.

**Vykonané overenia**

- Vstupná aj záverečná kontrola potvrdili požadovaný HEAD, AP gitlink, vetvu `main` a čistý pracovný strom.
- Prečítané boli všetky povinné aplikačné súbory a relevantné nadväzujúce implementácie a testy.
- V izolovanej pamäťovej databáze prešlo **38 existujúcich testov zo šiestich modulov za 5,26 sekundy**.
- Použité boli syntetické účty, testovací signing key a testovací password hasher. `.env` sa nenačítaval.
- Ďalšie sondy vykonali existujúci kód s pamäťovou databázou alebo s nahradeným `fetch` a store.
- Žiadna sonda nepoužila sieť, providera, skutočný credential ani súbor s lokálnymi secrets.
- Nebol spustený frontend build ani celý frontend Vitest suite.

```text
Resolved Execution Issues / Near-Misses:
- Delivery blocker resolved by explicit acceptance of chat delivery.
- One isolated AST probe initially lacked AST location metadata;
  corrected with ast.fix_missing_locations and rerun successfully.
- Exploratory searches naming absent candidate files were widened to
  the actual repository paths. These were search misses, not application failures.

Pre-Existing Failure Classification:
- Synthetic frontend probe confirmed stale refresh completion can restore
  cleared auth or overwrite a subsequently selected account.
- Isolated Django requests confirmed malformed simulation IDs produce
  HTTP 500 on step/action/stop.
- An absent, syntactically valid simulation UUID produces HTTP 500 on step.
- Synthetic output probes confirmed unrestricted diagnostic JSON copying
  and unrestricted forwarding of backend JSON error fields.
- The 38 selected existing regression tests passed.
```

## D1 — Inventár existujúcich a chýbajúcich kontrol

V tejto tabuľke `landed-tested` znamená, že v baseline existuje príslušný regresný test. Samostatná sonda môže potvrdiť správanie aj tam, kde trvalý regresný test zatiaľ chýba.

| Kontrola | Dôkaz v baseline | Stav | Záver pre Slice 1 |
|---|---|---|---|
| Anonymný prístup k admin games list | `_AdminAPIView`; `test_admin_games_list_requires_staff` | `landed-tested` | Zachovať 401; neopakovať rovnaký test. |
| Non-staff prístup k admin games list | Rovnaký test | `landed-tested` | Zachovať 403. |
| Anonymný/non-staff prístup k replay | `test_admin_game_replay_requires_staff` | `landed-tested` | Bez novej implementácie oprávnení. |
| Anonymný/non-staff simulation create | `test_create_requires_staff_and_returns_complete_initial_state` | `landed-tested` | Zachovať existujúci test. |
| Anonymný/non-staff analytics | `test_staff_boundary_contract_and_private_cache_headers` | `landed-tested` | Zachovať existujúci test. |
| Anonymný/non-staff simulation state, step, action a stop | Dedia `_SimulationAPIView`; zodpovedajúce negatívne API prípady v simulation testoch chýbajú | `landed-untested` | Doplniť parametrizované testy. |
| Neplatné a expirované JWT na admin API | `PasswordAwareJWTAuthentication`; izolované sondy vrátili 401 | `landed-untested` | Doplniť testy priamo cez Authorization header. |
| Zrušenie staff oprávnenia pri stále platnom JWT | JWT autentifikácia načítava aktuálneho používateľa; permission kontroluje aktuálne `is_staff` | `landed-untested` | Doplniť test demotion bez vydania nového tokenu. |
| PATCH `is_staff=False` vykonaný staff používateľom | `test_user_serializer_exposes_is_staff` | `landed-tested` | Pole zostáva read-only. |
| PATCH `is_staff=True` non-staff používateľom | `UserSerializer.Meta.read_only_fields`; sonda potvrdila zachovanie `False` | `landed-untested` | Doplniť trvalý regresný test. |
| PATCH `is_superuser`, groups, permissions a ďalšie neexponované polia | Explicitný `UserSerializer.Meta.fields`; sonda potvrdila ignorovanie | `landed-untested` | Testovať; nerozširovať serializer. |
| Registrácia s `is_staff=True` | `test_user_serializer_exposes_is_staff` | `landed-tested` | Neopakovať samostatný rovnaký prípad. |
| Registrácia s ďalšími privilegovanými poľami | `RegisterSerializer` obsahuje iba username/email/password | `landed-untested` | Doplniť prípady superuser, groups, permissions a service account. |
| Simulation step/stop iba pre tvorcu | `test_any_staff_can_read_but_only_creator_can_mutate` | `landed-tested` | Zachovať 404 pre iného staff. |
| Simulation action iba pre tvorcu, aj so známym lease | `_locked_lease` filtruje `created_by_id`; sonda staff B → 404 | `landed-untested` | Doplniť testy action operácií a nezmeneného lease. |
| Čítanie simulácie iným staff | `test_any_staff_can_read_but_only_creator_can_mutate` očakáva 200 | `product-choice` | Už prijaté správanie; nemení sa. |
| Lease sa nenachádza vo verejnom simulation state | `serialize_simulation_state` vracia iba `in_flight`; sonda potvrdila absenciu `lease_id` | `landed-untested` | Doplniť explicitný kontraktový test. |
| Odmietnutie nesprávneho, expirovaného alebo zastaraného lease | `_locked_lease` kontroluje UUID, čas a move count | `landed-untested` | Doplniť deterministické prípady bez sleep. |
| Chybné UUID simulácie | GET používa parsovanie; step/action/stop nie jednotne | `missing` | Sondy potvrdili 500; opraviť na 404. |
| Neexistujúce platné UUID pri step | `step_playground_simulation` nezachytáva `PlaygroundSimulation.DoesNotExist` | `missing` | Opraviť na 404. |
| Obídenie `AdminAccessGate` | UI gate volá `api.me`; serverové API majú samostatné permission kontroly | `landed-tested` | Priame API negatívne testy dokazujú podstatnú hranicu. UI gate nie je autorita. |
| Next.js turn bez Authorization | `rejects missing authentication before claiming a turn` | `landed-tested` | Zachovať. |
| Next.js turn s tokenom bez staff oprávnení | Route najskôr volá Django step a kontroluje HTTP status | `landed-untested` | Otestovať 401/403/404/409 pred delegovaním. |
| Next.js CPU vetva | `short-circuits CPU turns without invoking a provider` | `landed-tested` | Posilniť tvrdenie explicitným `POST` spy assertion. |
| Next.js LLM delegovanie | Route importuje `POST as executeAiMoveInternal`; existujúci mock exportuje iné meno | `landed-untested` | Opraviť mock a doplniť vykonaný pozitívny test LLM vetvy. |
| Refresh single-flight pri prekrytí | `refreshPromise`; sonda: dve 401, jeden refresh, dva retry | `landed-untested` | Doplniť test; mutex zachovať. |
| Refresh po logout/account switch | Výsledok refreshu bez kontroly pôvodnej identity zapisuje store | `missing` | Synteticky potvrdené; opraviť. |
| `NEXT_PUBLIC_` provider credentials | Vyhľadávanie v `frontend/src`, env template a Next config našlo iba verejnú API URL | `landed-untested` | Žiadny zistený provider secret export; doplniť úzky statický kontrakt. |
| Admin list a analytics explicitné výstupné polia | `serialize_admin_game`, `build_admin_analytics`, response serializer | `landed-untested` | Doplniť testy minimálneho výstupu; bez plošného prepisu. |
| Sanitizácia `Move.ai_metadata` | `sanitize_ai_metadata`; `test_inspection_trace_is_bounded_and_drops_unknown_fields` a API metadata testy | `landed-tested` | Znovu použiť; nevytvárať konkurenčný sanitizer. |
| Replay `DiagnosticPly.ai_trace` a `earlier_attempt_failures` | `_diagnostic_ply_payload` používa `deepcopy` | `missing` | Sonda potvrdila zachovanie neznámych secret polí a voľných reťazcov. |
| Simulation config pri vytvorení | `_slot_snapshot` a `create_playground_simulation` zostavujú konkrétne polia | `landed-untested` | Vstup je obmedzený; doplniť aj explicitnú výstupnú projekciu uloženého configu. |
| Next.js chybové JSON payloady | `simulationBackendRequest` a route vracajú backend objekt bez projekcie | `missing` | Obmedziť chybový kontrakt. Sonda potvrdila prenesenie ľubovoľného poľa. |
| Injection top-level `runtime_url` pri create | `test_strict_payload_and_conflict_return_no_partial_second_game` | `landed-tested` | Neopakovať presne tento prípad. |
| Nested URL/env/diagnostic target injection | `StrictSerializer`, `SimulationSlotSerializer`, uzavreté `kind` a katalógové páry | `landed-untested` | Doplniť negatívne prípady. |
| CSRF pri session-auth simulation mutáciách | `SessionAuthentication`; izolovaný POST bez CSRF → 403 | `landed-untested` | Doplniť API regression; nemení sa autentifikačný mechanizmus. |
| Simulation throttle scopes | Create/step/action majú scopes; `ScopedRateThrottle` a rates sú v settings | `out-of-slice` | Nie sú neviazané. Prevádzkové overenie patrí Slice 3. |

**Upresnenie Django Admin:** staršie `/admin/` modelové obrazovky majú aj model permissions. Napríklad `TestDiagnosticAdminPermissionsS6` testuje view/change permissions a CSRF. Tieto kontroly sa nesmú nahradiť jednoduchým `is_staff`. Pravidlo A2 sa pri tomto pláne uplatňuje na predmetné REST admin API; existujúce dodatočné kontroly Django Admin zostávajú zachované.

## D2 — Zostávajúca práca na privilege escalation

Autoritou pre tieto závery sú [accounts serializers](/home/agile/Projects/libretiles/backend/accounts/serializers.py) a [accounts authentication](/home/agile/Projects/libretiles/backend/accounts/authentication.py).

### Zachovať existujúce správanie serializerov

`UserSerializer` explicitne exponuje:

```text
id
username
email
preferred_ai_model_id
date_joined
is_staff
```

Read-only polia sú:

```text
id
date_joined
is_staff
```

`RegisterSerializer` prijíma iba:

```text
username
email
password
```

**Nenavrhuje sa produkčná zmena týchto serializerov.** Baseline už bráni hromadnému priradeniu privilegovaných polí.

Zachovať aj existujúcu kompatibilitu: neexponované alebo read-only polia sa pri týchto auth serializerových operáciách ignorujú. Nezavádzať kvôli týmto testom nové HTTP 400 pre dovtedy ignorované polia.

### PATCH test

Použiť bežného používateľa bez staff, superuser, groups alebo permissions. Parametrizovať tieto vstupy:

```text
is_staff: true
is_superuser: true
is_service_account: true
is_active: false
groups: [existujúca testovacia group]
user_permissions: [existujúca testovacia permission]
password: syntetické iné heslo
password_changed_at: syntetický dátum
id: id iného používateľa
date_joined: syntetický iný dátum
```

Každý prípad musí:

1. Poslať PATCH `/api/auth/me/`.
2. Očakávať 200.
3. Načítať používateľa z databázy.
4. Overiť, že chránená hodnota zostala nezmenená.
5. Overiť, že identita odpovede zostala identitou volajúceho.
6. Pri privilege prípadoch overiť následný GET `/api/admin/games/` → 403.
7. Pri `password` overiť `check_password` voči pôvodnému syntetickému heslu; neporovnávať ani nevypisovať hash.

Aspoň jeden prípad má spolu s nepovoleným poľom zmeniť dovolený `email`, aby test dokazoval úspešné spracovanie PATCH a súčasné ignorovanie privilegovaného vstupu.

### Register test

Nový test registrácie má pokryť najmä:

```text
is_superuser
is_service_account
groups
user_permissions
is_active
```

Po 201 musí novovytvorený používateľ mať štandardné bezpečné defaulty, žiadne priradené oprávnenia a heslo vytvorené štandardnou registračnou cestou.

Existujúci register test `is_staff=True` sa nebude kopírovať.

### JWT testy

Testy neplatného a expirovaného tokenu musia používať skutočný:

```text
Authorization: Bearer <syntetický testovací token>
```

Nepoužívať `force_authenticate` na prípady, ktorých predmetom je JWT validácia.

Pokryť:

- malformed token;
- platne podpísaný, ale expirovaný access token;
- staff token po odobratí `is_staff`;
- token používateľa po nastavení `is_active=False`.

Očakávania:

- malformed/expired/inactive → 401;
- aktívny používateľ po staff demotion → 403.

Expiry vytvoriť nastavením `exp` do minulosti. Nepoužiť `sleep`.

### Čo znovu neimplementovať

Existujúce token lifecycle testy už pokrývajú refresh rotation, odmietnutie starého refresh tokenu, logout blacklist a password-change revocation. Tieto mechanizmy neprepisovať.

Chýbajúci test nie je dôkaz chýbajúcej autorizácie. Produkčná auth oprava v tomto pláne sa týka frontendového nakladania s výsledkom refreshu, nie Django privilege policy.

## D3 — Staff horizontal isolation a Next.js turn proxy

Relevantné implementácie sú [simulation services](/home/agile/Projects/libretiles/backend/game/simulations.py) a [Next.js turn route](/home/agile/Projects/libretiles/frontend/src/app/api/admin/simulate/[id]/turn/route.ts).

### Existujúca hranica oprávnení

Zachovať tento model:

```text
Staff A vytvorí simuláciu.
Staff A aj Staff B môžu čítať jej admin state a replay.
Iba Staff A môže vykonať step/action/stop.
```

404 pri pokuse staff B o mutáciu je prijateľné fail-closed správanie. Nenahrádzať ho 403 iba kvôli jednotnej terminológii.

Izolovaná sonda navyše potvrdila:

```text
Staff B GET state: 200
State obsahuje lease_id: nie
Staff B action/release so známym lease Staff A: 404
Lease po pokuse: nezmenený
```

**Nebola preukázaná existujúca IDOR ani krádež lease medzi staff používateľmi.**

Lease UUID nie je samostatná autorizačná schopnosť. `_locked_lease` musí naďalej vyžadovať aj správneho tvorcu a zhodný stav ťahu.

### Jednotné spracovanie ID

V `simulations.py` zaviesť jeden privátny parser identifikátora simulácie a používať ho vo všetkých štyroch vstupných službách:

- `get_playground_simulation`;
- `step_playground_simulation`;
- `_locked_lease`;
- `stop_playground_simulation`.

Parser:

1. Prijíma textové game UUID.
2. Prevedie ho na `uuid.UUID`.
3. Chybný vstup preloží na `SimulationNotFoundError`.
4. Nevkladá pôvodný vstup ani exception text do verejnej odpovede.

Pri step používať už v databázovom lookup:

```text
game__public_id = parsed UUID
created_by_id = user_id
```

`PlaygroundSimulation.DoesNotExist` preložiť na `SimulationNotFoundError`, rovnako ako pri ostatných mutáciách.

Zachovať `select_for_update`, transakcie, lease kontrolu a pravidlá ťahu. Nezavádzať všeobecné zachytávanie každej exception ako 404; nesúvisiace programátorské chyby sa nesmú maskovať ako neexistujúci objekt.

Výsledná matica:

| Vstup | GET state | step | action | stop |
|---|---:|---:|---:|---:|
| Chybné UUID, oprávnený staff | 404 | 404 | 404 | 404 |
| Platné neexistujúce UUID | 404 | 404 | 404 | 404 |
| Existujúca obyčajná hra bez simulation záznamu | 404 | 404 | 404 | 404 |
| Simulácia iného staff | 200 | 404 | 404 | 404 |
| Vlastná simulácia s nesprávnym lease | — | Podľa aktuálneho in-flight stavu | 409 | Podľa existujúceho stop kontraktu |

### Next.js autorizačný tok

Existujúci tok je správny v podstatnej hranici:

```text
Authorization header
→ Django /step/
→ kontrola HTTP statusu
→ CPU odpoveď alebo LLM claim
→ interné AI vykonanie
→ Django /action/ pri každej privilegovanej operácii
```

Route sama nekontroluje `is_staff` a lokálne neoveruje podpis JWT. Autorizačnú kontrolu robí Django pri step a pri každom action.

**Nepridávať druhé, redundantné `/auth/me/` pred step.** Vytvorilo by ďalší request bez nahradenia objektovej autorizácie, ktorú aj tak musí vykonať step.

### Ohraničené zmeny proxy

1. Nahradiť lokálny jednoduchý Bearer parser existujúcim `bearerTokenFromAuthorizationHeader`.
2. Pred vytvorením backend cesty validovať route ID ako UUID; chybný identifikátor vrátiť ako 404.
3. Zachovať projekciu vstupného body na `expected_move_count`.
4. Neprijať z request body token, lease, provider, runtime model, URL ani credential konfiguráciu.
5. Zachovať získavanie modelu a budgetov z Django claim.
6. Pri neúspešnom claim nikdy nevolať interné AI vykonanie.
7. V action transporte vyhodnotiť HTTP status pred použitím `action.data`. Neúspešná odpoveď nesmie byť považovaná za úspech len preto, že jej JSON obsahuje napríklad `ok: true`.
8. Preložiť transportné chyby na pevný verejný chybový kontrakt podľa D4.
9. Zachovať `AsyncLocalStorage` transport; nepremiestniť token alebo lease do spoločnej mutovateľnej globálnej premennej.

Dodatočné polia Next.js request body sú dnes ignorované bezpečnou projekciou. Nie je potrebné zaviesť ich odmietanie, aby sa zabránilo runtime injection. Testovať sa má najmä to, že sa nedostanú do claim ani delegovaného requestu.

### Lease lifecycle

Nezavádzať automatické opakovanie mutácií ani nový mechanizmus uvoľňovania lease pri každej chybe.

Zachovať existujúce možnosti:

- úspešný terminal lease vyčistí;
- creator môže použiť `release`;
- stop lease vyčistí;
- expirovaný lease môže nahradiť nový oprávnený claim.

Test dvoch klientov má dokazovať, že druhý claim počas aktívneho lease dostane 409. SQLite test nie je dôkaz PostgreSQL súbežného row locking; to patrí do Slice 2.

## D4 — Secret minimization

### Rozlíšiť jednotlivé kategórie údajov

| Údaj | Pravidlo |
|---|---|
| Provider/model identifikátor, napr. `openrouter` | Legitímna súčasť verejného katalógu a admin diagnostiky. |
| Názov provider credential premennej | Nevracať v predmetných REST/SSE payloadovoch; netvrdiť, že samotný názov je credential hodnota. |
| Hodnota provider credential | Nikdy nevracať, nevkladať do testových reportov ani nečítať na účely sanitizácie. |
| Používateľský access/refresh token | Existujúci autentifikačný kontrakt; nesmie sa objaviť v admin odpovedi alebo SSE. |
| Obe racky v staff replay/simulation | Zamýšľaná administrátorská funkcionalita. |
| Súperov rack v bežnom game state | Zakázaný; bežný endpoint poskytuje iba vlastný `my_rack` a cudzie `rack_count`. |
| Lexikonový identifikátor a verejný upstream zdroj | Zachovať. Nezamieňať ich s lokálnou filesystem cestou. |
| Lokálna cesta, exception stack, raw provider response | Nevracať v predmetných diagnostických/chybových rozhraniach. |

Django Admin formulár pre `DiagnosticTarget` potrebuje výber `credential_env_name` na konfiguráciu registrovaného targetu. Tento plán neodstraňuje dané pole z existujúceho oprávneného konfiguračného formulára.

### Admin list a analytics

Existujúci admin list explicitne vyberá svoje polia. Analytics zostavuje agregované výsledky a používa response serializer.

Nenavrhuje sa nový generický serializer všetkých modelových atribútov ani plošný rewrite analytics.

Nové testy majú do nepoužívaných zdrojových JSON polí vložiť syntetické sentinely a overiť ich neprítomnosť vo výsledku:

```text
credential_env_name
api_key
authorization
raw_output
report_path
```

Použiť pritom platné model/provider identity, aby test nekonštruoval neexistujúcu požiadavku „redigovať ľubovoľný text aj v zámerne verejnom model_id“.

Analytics sa nesmie zmeniť na transport raw trace, configu, rackov, tokenov alebo diagnostic target konfigurácie.

### Replay diagnostické JSON

Konkrétna chýbajúca ochrana je v `_diagnostic_ply_payload`:

```text
earlier_attempt_failures → deepcopy(...)
ai_trace → deepcopy(...)
```

Izolovaná sonda existujúcej funkcie potvrdila, že neznáme secret polia, vnorený `api_key`, filesystem cesta aj voľný Bearer reťazec zostanú zachované.

**Dosah zistenia:** ide o preukázané správanie výstupnej funkcie pri syntetických dátach. Nebolo preukázané, že bežný používateľ dokáže do týchto konkrétnych stĺpcov vložiť skutočný serverový credential. Aktuálny diagnostic runner `ai_trace` pri `_persist_ply` neplní. Toto rozlíšenie musí zostať aj v implementačnom reporte.

Zvoliť explicitnú výstupnú projekciu, nie všeobecný regex, ktorý sľubuje nájsť každé tajomstvo.

**Kontrakt `ai_trace` pre tento slice:**

- `None` zostáva `null`.
- Objekt môže ponechať iba existujúcim pozitívnym testom doložený číselný `attempts`.
- `attempts` musí byť nezáporné celé číslo; Python `bool` sa nepovažuje za číslo.
- Pre interoperabilitu s JavaScriptom akceptovať iba bezpečne reprezentovateľné celé číslo.
- Neznáme kľúče, reťazce a vnorené objekty sa nevracajú.
- Objekt bez akceptovaného poľa sa zmení na `{}`.
- Nepodporovaný top-level typ sa zmení na `null`.

Tým zostane zachovaný existujúci pozitívny kontrakt:

```json
{"attempts": 1}
```

Existujúci podrobný trace pod `Move.ai_metadata.inspection_trace` zostáva spracovaný existujúcim `sanitize_ai_metadata`. Neprenášať ho do nového konkurenčného formátu.

**Kontrakt `earlier_attempt_failures`:**

- `None` zostáva `null`.
- Podporovaný je iba zoznam.
- Preniesť najviac tri položky.
- Ponechať iba tieto rozpoznané kódy:

```text
timeout
rate_limited
provider_auth_failed
provider_rate_limited
provider_unavailable
```

- Nerozpoznanú položku v prenášanom rozsahu nahradiť pevným `"redacted"`.
- Nevypisovať jej pôvodný obsah.
- Nepodporovaný top-level typ zmeniť na `null`.
- Zachovať poradie ponechaných položiek.

Tieto helpery umiestniť ako privátne funkcie do `replay.py`. Nemeniť databázu, runner ani historické záznamy.

Existujúce frontendové typy `JsonValue` a `z.json()` tento zúžený výstup prijímajú. Netreba meniť replay schema version.

### Simulation config

`serialize_simulation_state` dnes vracia celý uložený `config_json`. Pri súčasnom create je obsah zostavený serverom, takže nie je doložený vstupný injection bypass. Výstup však môže nechcene začať prenášať budúce interné polia.

Nahradiť priame vrátenie uloženého objektu novým objektom s explicitnými poľami:

```text
version
variant_slug
seed
ai_timeout
ai_max_steps
judge_mode
judge_model_id
slots
```

Pre každý slot ponechať iba:

```text
kind
provider
model_id
display_name
prompt_id
prompt_name
policy
```

`policy` sa prenesie iba tam, kde v platnom CPU snapshote existuje. Nevymýšľať hodnoty pre neexistujúce polia.

Pravidlá:

- Nemutovať uložený JSON počas serializácie.
- Nevracať pridané top-level ani slotové interné kľúče.
- Zachovať všetky existujúce legitímne hodnoty.
- Nepridávať opravu poškodených historických hier, obnovu rackov ani legacy fallback.
- Zachovať `racks` pre staff simulation view.
- Nepridávať `lease_id`, `leased_move_count` alebo `lease_expires_at` do state.

### Next.js chybové odpovede

V `admin-simulation-server.ts` zaviesť jednotný výsledok pre chybové odpovede. Raw backend `detail`, vnorené JSON objekty, HTML, headers a exception text sa nesmú vracať klientovi.

Použiť tieto pevné verejné správy:

| Stav | Verejný `detail` |
|---|---|
| 400 | `The simulation request was invalid.` |
| 401 | `Authentication credentials were invalid or expired.` |
| 403 | `Staff access is required.` |
| 404 | `Not found.` |
| 409 | `The simulation state changed. Reload and retry.` |
| 429 | `Too many simulation requests. Retry later.` |
| Backend 5xx alebo transportná chyba | `The simulation backend is unavailable.` |
| Neplatný úspešný backend payload | `The simulation backend returned an invalid response.` |

Pravidlá HTTP:

- Bežné uvedené 4xx zachovať.
- 409 navyše vráti pevné `code: "state_conflict"`.
- Backend 5xx a sieťová výnimka sa klientovi normalizujú na 503.
- Neplatný úspešný payload sa normalizuje na 502.
- Neočakávaný status sa nepovažuje za úspech.
- Nepreberať ďalšie kľúče z chybového JSON.
- Neúspešný action transport vyvolá výnimku obsahujúcu iba tento bezpečný status a správu.

Pre CPU úspech overiť aspoň existenciu očakávaného simulation state, jeho verziu a zhodu game ID pred emitovaním SSE. Autoritou kompletného úspešného state zostáva explicitná backendová serializácia.

Nezavádzať nový parser celého existujúceho AI SSE protokolu. Existujúce AI move testy už pokrývajú obmedzené interné chyby a neprítomnosť diagnostic target materiálu v SSE.

Na Next.js simulation odpovediach nastaviť:

```text
JSON: Cache-Control: private, no-store
SSE:  Cache-Control: private, no-store, no-transform
Vary: Authorization
```

Ide o ochranu konkrétneho citlivého payloadu v Slice 1. Globálne CSP, HSTS a deployment headers zostávajú v Slice 3.

### Client bundle a secrets

Vyhľadávanie našlo v aplikačnom `NEXT_PUBLIC_` rozhraní iba `NEXT_PUBLIC_API_URL`. Next config nemá vlastný export serverových credentials cez `env` alebo runtime config.

Doplniť úzky statický test nad `frontend/src`, ktorý akceptuje iba tento názov `NEXT_PUBLIC_` premennej. Nečítať `.env.local` ani existujúce build artefakty na hľadanie skutočných credentials.

Nepridávať dependency ani vykonávať build len kvôli tomuto testu.

Skutočná dostupnosť credentials zostáva:

```text
present: unknown — OPENROUTER_API_KEY
present: unknown — NVIDIA_API_KEY
present: unknown — GROQ_API_KEY
present: unknown — GEMINI_API_KEY
present: unknown — CLOUDFLARE_API_TOKEN
present: unknown — MISTRAL_API_KEY
present: unknown — IBM_CLOUD_API_KEY
present: unknown — AION_API_KEY
present: unknown — HF_TOKEN
present: unknown — DJANGO_SECRET_KEY
```

## D5 — Token refresh single-flight a ochrana relácie

Relevantná implementácia je [api.ts](/home/agile/Projects/libretiles/frontend/src/lib/api.ts).

### Čo existujúci mutex dokazuje

Sonda nad existujúcim modulom, so syntetickým store a nahradeným `fetch`, vrátila:

| Scenár | Pozorovanie |
|---|---|
| Dve prekrývajúce sa 401 | Jeden refresh, dve opakovania pôvodných requestov |
| Druhá stará 401 príde po ukončení refreshu | Druhý refresh request |
| Logout počas refreshu | Dokončený refresh obnovil token |
| Zmena účtu počas refreshu | Dokončený refresh prepísal token nového účtu |

Druhý riadok sám osebe neznamená pokazený single-flight: requesty už v čase refreshu neboli prekryté. Posledné dva riadky však dokazujú chýbajúcu ochranu výsledku patriaceho starej relácii.

### Zvolený návrh

Zachovať jeden spoločný Promise pre refresh **v rámci aktuálnej relácie**. Nezavádzať knižnicu, frontu requestov, globálny retry orchestrátor ani nový spôsob uloženia tokenov.

Rozšíriť store o malú prechodnú identitu relácie:

```ts
authEpoch: number
```

Vlastnosti:

- Inicializácia na `0`.
- Nezapisovať do `partialize`.
- Nemení sa persisted store version.
- `setToken`, `setRefreshToken` a `clearAuth` zvyšujú epoch.
- Úspešná automatická rotácia tokenov v tej istej relácii epoch nemení.
- Pri hydration sa epoch nesmie prebrať z persisted údajov. Ak hydration zmení tokenovú dvojicu, epoch sa zvýši.
- Epoch je lokálny identifikátor asynchrónnej práce; nie je bezpečnostnou autoritou servera.

Doplniť store action pre atómové prijatie refresh výsledku:

```ts
type AuthSnapshot = {
  epoch: number;
  token: string | null;
  refreshToken: string | null;
};

applyRefreshedAuth(
  expected: AuthSnapshot,
  next: { access: string; refresh?: string },
): boolean;
```

Action v jednom funkčnom store update:

1. Porovná aktuálny epoch, access token aj refresh token s `expected`.
2. Pri nezhode nič nezmení a vráti `false`.
3. Pri zhode naraz aktualizuje access aj prípadný refresh token.
4. Ak refresh pole v odpovedi chýba, ponechá existujúci refresh token.
5. Nezvýši epoch.
6. Vráti `true`.

Existujúce verejné setter funkcie ostávajú k dispozícii login a logout obrazovkám. Tieto obrazovky sa nemenia.

### Algoritmus `request`

Pred prvým odoslaním requestu:

1. Zachytiť aktuálny epoch iba vtedy, ak `opts.token` zodpovedá aktuálnemu store tokenu.
2. Ak request nesie iný explicitný token, nesmie sa neskôr automaticky obnovovať pomocou refresh tokenu aktuálne prihláseného účtu.
3. Odoslať pôvodný request bez zmeny jeho existujúceho kontraktu.

Po 401:

1. Bez tokenu žiadny refresh.
2. Bez zodpovedajúcej zachytenej relácie žiadny refresh.
3. Ak sa epoch zmenil, žiadny refresh ani retry pod novou identitou.
4. Ak epoch zostal rovnaký a store už obsahuje nový access token po inom úspešnom refreshi, použiť tento token na jedno opakovanie.
5. Inak získať alebo zdieľať refresh Promise patriaci zachytenej relácii.
6. Pred retry znovu overiť epoch a zhodu aktuálneho access tokenu s výsledkom refreshu.
7. Pri zmene relácie výsledok ignorovať.
8. Každý pôvodný request smie byť opakovaný najviac raz.
9. Druhá 401 už nespustí ďalšie kolo obnovy toho istého requestu.

Tým sa pokryje aj oneskorená stará 401 bez zbytočnej druhej rotácie.

### Vlastníctvo spoločného Promise

Pri Promise evidovať aj jeho vlastniaci epoch.

- Requesty tej istej relácie zdieľajú jeden in-flight Promise.
- Nová relácia nesmie dostať Promise starej relácie.
- Nová relácia môže začať vlastný refresh, aj keď starý ešte dobieha.
- Starý výsledok musí zlyhať na porovnaní snapshotu.
- Starý `finally` nesmie vymazať novší Promise.

Cleanup preto používa porovnanie identity:

```ts
if (refreshPromise === thisFlight) {
  refreshPromise = null;
  refreshOwnerEpoch = null;
}
```

Vytvorenie Promise má odložiť vykonanie práce do microtasku, aby bolo vlastníctvo nastavené aj pri synchrónnej výnimke testovacieho `fetch`:

```ts
const thisFlight: Promise<string | null> = Promise.resolve()
  .then(() => performRefresh(snapshot))
  .finally(() => {
    if (refreshPromise === thisFlight) {
      refreshPromise = null;
      refreshOwnerEpoch = null;
    }
  });

refreshPromise = thisFlight;
refreshOwnerEpoch = snapshot.epoch;
```

`performRefresh` musí zachytiť očakávané transportné zlyhania a vracať `null`; nepridávať neobslúžené odmietnuté Promise cez samostatný nepoužitý `.finally()`.

### Prijatie a odmietnutie odpovede

Pred zápisom:

- `access` musí byť neprázdny reťazec.
- Ak je `refresh` prítomný, musí byť neprázdny reťazec.
- Malformed JSON alebo neplatný tvar sa nesmie uložiť do store.

Pri HTTP failure alebo malformed úspešnej odpovedi:

- vyčistiť auth iba vtedy, ak store stále zodpovedá pôvodnému snapshotu;
- nikdy nevyčistiť novší účet.

Pri transportnej výnimke:

- zachovať existujúce správanie: vrátiť `null` bez automatického vymazania uložených tokenov;
- nepremeniť dočasnú nedostupnosť siete na novú logout policy.

### Najmenší test single-flight

Test musí mať dve samostatné bariéry:

1. Obe pôvodné volania `api.me` dostanú 401.
2. Refresh odpoveď zostáva zadržaná, kým obe volania nedosiahnu refresh vetvu.

Potom:

- pred uvoľnením refreshu overiť jeden refresh request;
- uvoľniť jednu platnú odpoveď s novou tokenovou dvojicou;
- počkať na oba requesty;
- overiť dva retry s novým access tokenom;
- overiť jeden refresh celkovo a aktualizovanú tokenovú dvojicu.

Test s dvoma okamžite hotovými odpoveďami bez kontrolovaného poradia neposkytuje dostatočný dôkaz single-flight.

Táto ochrana je v rámci jedného načítaného store/runtime. Nezavádza cross-tab koordináciu ani nový session storage produktový model.

## D6 — Playground injection a diagnostic targets

### Existujúci kontrakt

`SimulationCreateSerializer` a `SimulationSlotSerializer` používajú `StrictSerializer`.

Z toho vyplýva:

- top-level neznáme pole → 400;
- neznáme pole v slote → 400;
- `kind` je iba `cpu | llm`;
- CPU slot nesmie niesť dodatočné provider/prompt polia;
- LLM slot musí zodpovedať selectable provider/model páru;
- prompt preset musí byť selectable;
- creator pochádza z `request.user.id`.

### Konkrétne testované vstupy

| Miesto vstupu | Príklad kategórie | Očakávanie |
|---|---|---|
| Create root | `created_by_id`, `credential_env_name`, `diagnostic_target_id` | 400 |
| LLM slot | `runtime_url`, `base_url`, `credential_env_name`, `diagnostic_target`, `diagnostic_target_id` | 400 |
| LLM provider | URL alebo IP namiesto provider identifikátora | 400 ako neznámy pár |
| LLM model | URL namiesto selectable model ID | 400 |
| Slot kind | `diagnostic`, `target`, iná nepovolená hodnota | 400 |
| CPU slot | provider/model/prompt pole, aj explicitne uvedené nepovolené null | 400 podľa existujúceho kontraktu |
| Step/action | `user_id`, `slot`, runtime alebo model override | 400 |
| Next.js turn body | extra runtime/target/token/lease polia | Nedostanú sa do delegovaného vstupu ani claim |

Použiť syntetické hodnoty vrátane loopback URL a platne vyzerajúceho target UUID. **Nesmie sa na tieto adresy vykonať DNS alebo HTTP.**

Pri odmietnutom create overiť:

```text
GameSession count nezmenený
PlayerSlot count nezmenený
PlaygroundSimulation count nezmenený
DNS resolver nevolaný
provider/runtime nevolaný
```

### Diagnostic target rozhodnutie

Playground LLM sloty zostávajú katalógové. Diagnostic target sa pre ne neprijíma.

To je existujúci kontrakt, nie nové produktové rozhodnutie. Nenavrhuje sa odomknutie diagnostic target runtime, zmena fake/live režimu runnera ani pridanie credential env výberu do playground UI.

Playground create sa pri tomto kontrakte nedostane do URL policy diagnostic targetov. Preto:

- nekopírovať `diagnostic_ssrf_cases.json` do nového playground testu;
- nemení sa `diagnostic_targets.py`;
- nemení sa bound HTTPS adapter;
- existujúca S7 SSRF sada zostáva samostatná.

## D7 — Testovacia matica

### Súbory

Nový backend testovací modul:

```text
backend/tests/test_admin_infosec_hardening.py
```

Jediný frontend testovací súbor rozširovaný týmto slice:

```text
frontend/src/app/api/admin/simulate/[id]/turn/route.test.ts
```

Frontend súbor rozdeliť pomocou samostatných `describe` blokov na refresh lifecycle, proxy autorizáciu, proxy payloady a statické public-env pravidlo. Tým sa zachová jedna frontend testovacia cesta podľa zadania.

### Backend test fixtures

Použiť:

- anonymous klienta;
- bežného používateľa;
- staff A;
- staff B;
- dve oddelené `APIClient` inštancie pre tvorcu pri lease teste;
- jeden explicitne selectable LLM pár zo seedovaného offline katalógu;
- simuláciu s oboma LLM slotmi pre lease prípady, aby starting slot neovplyvnil test;
- pevný seed;
- pamäťovú databázu;
- syntetické credentials a lokálny cache.

Nevykonávať LLM ani CPU search, ak ho daný test nepotrebuje. Pre testy odmietnutia majú drahé alebo externé volania spy, ktorý zlyhá, ak sa vôbec zavolá.

### Nové backend testy

| Názov testu / skupiny | Aktér | Request | Stav | Povinné assertion |
|---|---|---|---:|---|
| `test_nonstaff_patch_cannot_change_privileged_fields` | user | PATCH `/auth/me/`, prípady D2 | 200 | Chránené DB polia nezmenené; následný admin request 403. |
| `test_patch_ignores_privilege_fields_while_updating_email` | user | PATCH s email + privilege poľom | 200 | Email zmenený, privilege nie. |
| `test_register_ignores_unexposed_user_fields` | anon | POST register, prípady D2 | 201 | Bez superuser/service-account/groups/permissions. |
| `test_admin_routes_reject_invalid_access_token` | invalid JWT | Osem admin endpointov | 401 | Bez mutácie a bez provider práce. |
| `test_admin_routes_reject_expired_access_token` | expired staff JWT | Rovnaké endpointy | 401 | Rovnaké assertion; expiry bez sleep. |
| `test_demoted_staff_token_loses_admin_access` | bývalý staff A | GET admin list + POST action | 403 | Starý platný JWT neudrží staff právo. |
| `test_inactive_staff_token_is_rejected` | inactive staff A | GET list + POST action | 401 | Bez mutácie. |
| `test_simulation_remaining_endpoints_require_staff` | anon/user | state, step, action, stop | 401/403 | Pokryť chýbajúce endpointy; nekopírovať create test. |
| `test_session_simulation_mutations_require_csrf` | staff A session | create/step/action/stop bez CSRF | 403 | Nezmenený stav; použiť `enforce_csrf_checks=True`. |
| `test_staff_cannot_use_another_creators_lease` | staff B | action s platným známym lease A | 404 | Žiadna zmena move count, rackov, skóre alebo lease. |
| `test_simulation_state_never_exposes_lease_material` | staff A/B | GET state počas lease | 200 | `in_flight=True`; tri interné lease polia neprítomné. |
| `test_second_client_cannot_claim_an_inflight_turn` | staff A, dva klienty | dva step requesty | 200, 409 | Prvý lease nezmenený; nulový počet nových moves. |
| `test_wrong_lease_is_rejected` | staff A | action s iným UUID lease | 409 | Stav nezmenený. |
| `test_expired_lease_is_rejected` | staff A | action s expirovaným lease | 409 | Čas nastaviť v DB, bez čakania. |
| `test_stale_move_count_is_rejected` | staff A | action/step so starým count | 409 | Žiadny ďalší move. |
| `test_released_lease_cannot_be_reused` | staff A | release, potom action so starým lease | 200, 409 | Lease vyčistený; reuse odmietnutý. |
| `test_expired_lease_can_be_reclaimed_by_creator` | staff A | step po expiry | 200 | Nový lease; starý action stále 409. |
| `test_simulation_identifiers_return_controlled_404` | staff A | state/step/action/stop; malformed, absent, ordinary-game ID | 404 | Žiadny traceback, žiadna mutácia; CPU step nevolaný. |
| `test_create_rejects_nested_runtime_and_target_injection` | staff A | nested prípady D6 | 400 | Žiadne čiastočné vytvorené objekty, DNS ani runtime. |
| `test_create_rejects_owner_and_credential_overrides` | staff A | root prípady D6 | 400 | Creator sa nedá nahradiť. |
| `test_slot_kind_and_catalog_pair_fail_closed` | staff A | nepovolený kind/provider/model/CPU extras | 400 | Bez runtime práce. |
| `test_simulation_actions_reject_identity_overrides` | staff A | step/action s dodatočnými identitnými poľami | 400 | Žiadna mutácia. |
| `test_replay_projects_diagnostic_trace` | staff A | GET replay s kontaminovaným syntetickým `ai_trace` | 200 | Zachová `attempts:1`, odstráni všetok ostatný testovací obsah. |
| `test_replay_bounds_failure_codes` | staff A | replay s rôznymi failure vstupmi | 200 | Whitelist, `"redacted"`, limit tri, zachovanie null. |
| `test_admin_list_and_analytics_exclude_internal_payloads` | staff A | GET list/analytics s kontaminovanými zdrojovými JSON poliami | 200 | Sentinely a interné kľúče neprítomné. |
| `test_simulation_config_output_is_projected` | staff A/B | GET po pridaní interných root/slot config polí do fixture | 200 | Verejné config hodnoty zachované, interné odstránené. |
| `test_regular_state_excludes_replay_and_opponent_racks` | participant user | GET `/api/game/{id}/` | 200 | Iba vlastný `my_rack`; bez replay snapshotov, bag seed/tiles a rack arrays. |
| `test_staff_status_does_not_bypass_regular_game_membership` | staff outsider | GET obyčajnej cudzej hry | 404 | Staff read-all zostáva na admin endpointoch. |

Osem endpointov pre JWT maticu znamená games list, replay, analytics a päť simulation endpointov: create, state, step, action, stop.

Pri action testoch iného staff používať validný serializerový vstup. Napríklad pre place/validate platne tvarované placements. Inak by 400 z validácie zamaskovalo neotestovanú creator kontrolu.

### Existujúce backend testy, ktoré sa nekopírujú

Použiť ako zachované regresie:

- `test_admin_games_list_requires_staff`;
- `test_admin_game_replay_requires_staff`;
- `test_create_requires_staff_and_returns_complete_initial_state`;
- `test_any_staff_can_read_but_only_creator_can_mutate`;
- `test_strict_payload_and_conflict_return_no_partial_second_game`;
- `test_staff_boundary_contract_and_private_cache_headers`;
- `test_user_serializer_exposes_is_staff`;
- `test_inspection_trace_is_bounded_and_drops_unknown_fields`;
- existujúce token lifecycle testy.

Test bežného racku sa dopĺňa o explicitné neprítomné polia, pretože existujúci `test_game_state_is_user_derived_and_hides_opponent_rack` hlavne porovnáva vlastné racky a cudzie rack count.

### Frontend testy refreshu

Všetky requesty majú nahradený `fetch`. Neočakávaná URL musí vyvolať chybu testu.

| Názov / scenár | Aktér | Simulovaná odpoveď | Očakávanie |
|---|---|---|---|
| `shares_one_refresh_for_overlapping_401s` | aktuálna relácia | dve 401, zadržaný refresh 200 | Jeden refresh, dva retry. |
| `reuses_rotated_access_for_late_stale_401` | tá istá relácia | druhá stará 401 až po dokončení refreshu | Žiadny druhý refresh; retry s aktuálnym tokenom. |
| `allows_a_later_independent_refresh_wave` | tá istá relácia | druhé neskoršie expiry | Nový refresh funguje; Promise bol vyčistený. |
| `does_not_refresh_tokenless_requests_or_403s` | anon/user | 401 bez tokenu alebo 403 | Žiadny refresh. |
| `retries_each_request_at_most_once` | user | retry opäť 401 | Žiadna slučka ďalších refreshov. |
| `clears_only_own_auth_on_rejected_refresh` | aktuálna relácia | refresh HTTP failure | Auth sa vyčistí iba vlastníkovi. |
| `rejects_malformed_refresh_payload` | aktuálna relácia | non-JSON, missing/empty/non-string token | Žiadna neplatná hodnota v store. |
| `preserves_auth_on_transport_failure` | aktuálna relácia | rejected fetch | Zachované tokeny; bounded failure. |
| `ignores_refresh_success_after_logout` | A → logout | oneskorené 200 | Auth zostane prázdny; pôvodný request sa neopakuje. |
| `ignores_refresh_success_after_account_switch` | A → B | oneskorené 200 pre A | Tokeny B nezmenené. |
| `old_refresh_failure_does_not_clear_new_account` | A → B | oneskorené failure pre A | Tokeny B nezmenené. |
| `new_account_does_not_join_old_refresh` | A → B | oba refresh in-flight | B používa vlastný flight. |
| `old_cleanup_does_not_clear_new_flight` | A → B | A skončí pred B, pribudne ďalšia B 401 | Ďalší B request zdieľa B flight. |
| `does_not_refresh_an_explicit_token_from_another_session` | request A, store B | 401 | Nepoužiť refresh B na request A. |
| `auth_epoch_is_transient_and_hydration_invalidates_old_work` | store lifecycle | login/logout/hydration/rotation | Epoch nie je persisted; refresh ho nemení; nová identita áno. |

Použiť reálny Zustand store, nie mock, ktorý obchádza novú ochranu. Medzi testami obnoviť počiatočný stav a vyčkať na všetky vytvorené Promise.

Nevystavovať nový produkčný „reset refresh mutex for tests“ export.

### Frontend testy proxy

Opraviť existujúci mock:

```ts
vi.mock("@/app/api/ai/move/route", () => ({
  POST: executeAiMoveMock,
}));
```

Mock musí exportovať meno `POST`, pretože práve to route importuje. Existujúci export `executeAiMoveInternal` nedokazuje funkčnosť LLM vetvy.

Existujúce testové ID `game-1` nahradiť pevným platným UUID, pretože skutočná backendová cesta používa game UUID.

| Scenár | Aktér / backend odpoveď | Očakávanie |
|---|---|---|
| Missing/malformed Authorization | anon | 401 bez backend claim a bez AI delegate. |
| Neplatné route UUID | staff header | 404 bez backend requestu. |
| Neplatný `expected_move_count` | staff header | 400 bez claim. |
| Django claim 401/403/404/409/429 | príslušný odmietnutý aktér/stav | Zachovaný kontrolovaný status; AI delegate nevolaný. |
| Chybový status s úspešne vyzerajúcim body | napr. 403 + `kind: llm` | Stále odmietnutie; žiadne AI vykonanie. |
| Platný CPU claim | staff A | SSE done, nula provider requests, AI delegate nevolaný. |
| Neplatný CPU state alebo LLM claim | backend 200 s chybným tvarom | 502 bez AI vykonania. |
| Platný LLM claim | staff A | AI `POST` volaný raz; parametre iba z claim a route identity. |
| Body obsahuje token/lease/runtime overrides | staff A | Overrides sa nepoužijú. |
| Action transport | staff A | Zachová route game ID, creator bearer a claim lease; premieta len operation payload. |
| Action HTTP failure s `ok:true` body | backend failure | Failure sa nesmie interpretovať ako commit. |
| Dva súbežné requesty pre odlišné simulácie | staff A/B | Reálny `AsyncLocalStorage` zachová oddelené tokeny, ID a lease. |
| Backend JSON error obsahuje syntetické secret polia | ľubovoľné odmietnutie | Žiadny sentinel v odpovedi. |
| Backend HTML alebo thrown exception obsahuje path/sentinel | transport | Pevná 502/503 správa, bez raw textu. |
| Citlivé response headers | JSON aj SSE | Očakávané `Cache-Control` a `Vary`. |
| Public env zdrojový kontrakt | bez aktéra | Jediný aplikačný názov je `NEXT_PUBLIC_API_URL`. |

LLM mock má vykonať testovací transport cez skutočný `currentAiMoveBackendTransport()`, aby pozitívny test overil väzbu medzi route a transportom. Nesmieme mockovať práve mechanizmus, ktorého izoláciu chceme dokázať.

### Rýchlosť a interpretácia

- Žiadne live providery, DNS, sieťové záťaže ani 1000-client testy.
- Žiadne sleep pre JWT alebo lease expiry.
- Nevytvárať nové benchmarky.
- Existujúce benchmark opt-in flags ostávajú vypnuté.
- Dvojklientový lease test nie je certifikácia SQL súbežnosti na PostgreSQL.
- Čas fast suite merať pred a po zmene za rovnakých podmienok.
- Ak baseline prekračuje 30 sekúnd, uviesť pre-existing klasifikáciu; neskrývať to zmenou výberu testov až po implementácii.

## D8 — Návrh implementačného grantu

### Poradie vykonania

1. **Nový execution grant a nový Worker.** Orchestrator vydá explicitný prompt s `Native planning mode: not-used`, `fresh-worker-session`, presným baseline a týmto zmrazeným plánom. Tento report sám implementáciu neautorizuje.
2. **Preflight.** Overiť HEAD, AP pin, vetvu, čistotu stromu a dostupnosť projektových nástrojov. Bez dependency install.
3. **Baseline overenie.** Spustiť existujúce zasiahnuté testy a stanovený fast test výber v izolovanom prostredí. Zaznamenať čas a prípadné pre-existing failures.
4. **Pridať backend negatívne testy.** Oprávnenia, injection a lease kontroly majú prevažne prejsť už pred zmenou. UUID a výstupné minimizačné prípady majú odhaliť pomenované nedostatky.
5. **Opraviť simulation ID a výstupné projekcie.** Bez zmeny WordAuthority, DB modelov alebo creator policy.
6. **Pridať frontend refresh regresie a implementovať ochranu relácie.** Zachovať Promise, doplniť epoch a atómové prijatie výsledku.
7. **Opraviť proxy mock, doplniť LLM/proxy negatívne testy a obmedziť error payloady.**
8. **Overiť kompatibilitu.** Existujúci replay `ai_trace={"attempts":1}`, CPU state, staff B GET, běžný `my_rack`, single-flight a token lifecycle musia zostať funkčné.
9. **Spustiť finálne gates a skontrolovať diff.** Každá zmena musí byť v allowliste a mať odôvodnenie v tomto pláne.
10. **Odovzdať implementačné dôkazy.** Bez samostatného tvrdenia nezávislej acceptance.
11. **Čerstvý zameraný bezpečnostný audit.** Orchestrator ho zadá na presný výsledný candidate podľa E3/R3.

### Presný mutation allowlist

| Cesta | Povolený účel |
|---|---|
| `backend/game/simulations.py` | Jednotné UUID/not-found spracovanie, creator-filtered step lookup, verejná projekcia configu. |
| `backend/game/replay.py` | Privátne bounded projekcie diagnostických JSON polí. |
| `backend/tests/test_admin_infosec_hardening.py` | Nová backend negatívna a kontraktová sada podľa D7. |
| `frontend/src/hooks/useGameStore.ts` | Nepersistovaný auth epoch, guarded atomic refresh update, hydration invalidation. |
| `frontend/src/lib/api.ts` | Vlastníctvo refresh flight, ochrana výsledku relácie, bounded retry a validácia tokenového payloadu. |
| `frontend/src/lib/admin-simulation-server.ts` | Kontrolované backend error payloady a transportné zlyhania. |
| `frontend/src/app/api/admin/simulate/[id]/turn/route.ts` | Bearer parser reuse, UUID check, status-aware transport, bezpečné chyby a cache headers. |
| `frontend/src/app/api/admin/simulate/[id]/turn/route.test.ts` | Jediná frontend testovacia cesta tohto slice; všetky frontend prípady D7. |

**Mimo allowlistu zostávajú** auth backend implementácia, Django modely/migrácie, `gamecore`, diagnostic target policy a adapter, katalógová selekcia, provider runtime implementácie, pravidelné hráčske stránky, dependency manifesty, lockfiles, `.ap`, env súbory a deployment skripty.

Ak test odhalí potrebu zmeny mimo tohto allowlistu, Worker ju nesmie potichu vykonať. Má odovzdať presný dôkaz a žiadať ohraničené rozšírenie grantu.

### API, typy a kompatibilita

- Nepribúda endpoint.
- Django staff/creator policy sa nemení.
- Auth PATCH/register zachovajú existujúce statusy a ignorovanie neexponovaných polí.
- Chybné/neexistujúce simulation ID budú vracať 404 namiesto 500.
- Next.js simulation chyby budú mať kontrolovaný verejný obsah.
- Replay JSON sa zúži podľa D4; existujúci doložený pozitívny trace zostáva.
- Simulation config zachová existujúce verejné polia.
- Store dostane interné `authEpoch` a guarded action; persisted shape a verzia sa nemenia.
- Nepribúda databázová migrácia.
- Nemení sa ukladanie access/refresh tokenov na cookies ani iný storage model.

### Overovacie príkazy a izolácia

Nasledujúce príkazy patria do **budúceho implementačného grantu**.

Bežné spustenie Django testov alebo mypy pluginu importuje `config.settings`, ktoré volá `load_dotenv`. Pri zachovaní zákazu čítania `.env` preto grant musí výslovne používať nasledujúci izolovaný bootstrap. Je založený na rovnakom princípe, aký už používa `test_security_settings.py`.

Z `backend/`:

```bash
env -u APPIMAGE -u ARGV0 -u APPDIR .venv/bin/ruff check .
```

Pre Python gates použiť projektovú `.venv/bin/python`, čisté prostredie, syntetické settings a zakázané načítanie dotenv pred importom Django:

```bash
env -i -u APPIMAGE -u ARGV0 -u APPDIR \
  PATH=/usr/bin:/bin \
  LANG=C.UTF-8 \
  IHR_GATE=focused \
  .venv/bin/python -B - <<'PY'
import os
import sys
import time

import dotenv

dotenv.load_dotenv = lambda *args, **kwargs: False

gate = os.environ["IHR_GATE"]

os.environ.update({
    "DJANGO_SETTINGS_MODULE": "config.settings",
    "DJANGO_SECRET_KEY":
        "TEST-ONLY-synthetic-django-secret-key-not-for-production-00000",
    "DJANGO_DEBUG": "true",
    "DJANGO_ALLOWED_HOSTS": "testserver,localhost,127.0.0.1",
    "DB_ENGINE": "sqlite3",
})

from config import settings as project_settings

project_settings.DATABASES["default"]["NAME"] = ":memory:"
project_settings.PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

started = time.monotonic()

if gate == "mypy":
    from mypy import api as mypy_api

    output, errors, result = mypy_api.run([
        "config", "game", "gamecore", "accounts", "catalog",
    ])
    sys.stdout.write(output)
    sys.stderr.write(errors)

elif gate in {"focused", "fast"}:
    import pytest

    args = ["-q", "-p", "no:cacheprovider", "--assert=plain"]

    if gate == "focused":
        args += [
            "tests/test_admin_infosec_hardening.py",
            "tests/test_admin_replay_api.py",
            "tests/test_admin_simulation_api.py",
            "tests/test_admin_analytics_api.py",
            "tests/test_admin_analytics_aggregation.py",
            "tests/test_simulation_services.py",
            "tests/test_move_inspection.py",
            "tests/test_token_lifecycle.py",
            "tests/test_api.py",
        ]
    else:
        args += ["-m", "not slow and not internet"]

    result = pytest.main(args)

else:
    raise SystemExit("Unknown IHR_GATE")

print(f"gate_elapsed_seconds={time.monotonic() - started:.2f}")
raise SystemExit(result)
PY
```

Tento istý blok vykonať s presne určenými režimami:

```text
IHR_GATE=mypy
IHR_GATE=focused
IHR_GATE=fast
```

Pri baseline focused behu pred vytvorením nového modulu sa vynechá iba ešte neexistujúci `test_admin_infosec_hardening.py`. Baseline a candidate fast výber musia byť rovnaké.

Syntetický MD5 hasher je iba zrýchlenie izolovaných testov. Nesmie sa dostať do produkčných settings alebo commitnutého runtime nastavenia.

Z `frontend/`:

```bash
npm run typecheck
npm run lint
npm run test -- \
  'src/app/api/admin/simulate/[id]/turn/route.test.ts' \
  src/lib/api.test.ts \
  src/lib/api-auth.test.ts \
  src/lib/admin-api.test.ts \
  src/lib/admin-access.test.ts \
  src/lib/admin-simulation.test.ts \
  src/lib/admin-replay.test.ts \
  src/lib/admin-analytics.test.ts \
  src/app/api/ai/move/route.test.ts \
  src/lib/ai-turn-simulation.test.ts
```

Existujúci `vitest.config.ts` používa `envDir` mimo `frontend/.env.local`. Túto ochranu zachovať.

Ďalšie pravidlá:

- Nevykonávať `npm run build` v tomto grante.
- Nepoužívať `npx`, ktorý by mohol doinštalovať chýbajúci nástroj.
- Chýbajúca dependency znamená presný blocker, nie povolenie na install.
- Nespúšťať live probe script.
- Nepoužívať ambient Python alebo Poetry ako alternatívnu execution route.
- Žiadne migrations proti existujúcej lokálnej alebo produkčnej databáze.
- Git diff a status kontrolovať bez stage, commit alebo push, pokiaľ nový grant tieto operácie výslovne nepridá.

### Acceptance kritériá pre implementáciu

Implementácia môže dostať svoj ohraničený implementation PASS iba ak:

1. Všetky nové negatívne testy prejdú.
2. Existujúce zasiahnuté testy zostanú zelené.
3. Logout/account switch počas refreshu nemôže obnoviť alebo prepísať auth.
4. Starý flight cleanup nemôže zrušiť vlastníctvo nového flight.
5. Prekrývajúce sa 401 v jednej relácii stále vyvolajú iba jeden refresh.
6. Chybné a neexistujúce simulation ID už nespôsobujú pomenované 500.
7. Staff B nemôže mutovať ani so známym platným lease staff A.
8. Staff B naďalej môže čítať simulation state.
9. Žiadny nový výstupný test nevráti vložené syntetické secret/path sentinely.
10. Regular game state zostane obmedzený na vlastný rack.
11. Playground nevykoná runtime alebo DNS pre odmietnutý injection vstup.
12. Fast suite splní 30-sekundový cieľ za dohodnutých rovnakých podmienok; prípadný baseline problém je explicitne klasifikovaný.
13. Diff zostane v allowliste.
14. Neuskutoční sa žiadny provider, sieťový, deployment ani credential side effect.

### Evidence tier a INFOSEC route

**Plánovací exchange:** E0, non-independent. Toto sa nemení tým, že plán obsahuje bezpečnostné zistenia.

**Navrhovaná implementácia:** **E3**, pretože po skutočnom prieskume nejde iba o testy. Mení sa správanie pri token/session hranici a zúženie prenášaných diagnostických údajov.

**Primárna INFOSEC route:** **R3 — fresh focused audit**, s R1 kontrolami počas implementácie.

Odôvodnenie:

- Boli synteticky potvrdené chyby pri výsledku refreshu po zmene relácie.
- Ich oprava zasahuje session/token lifecycle.
- INFOSEC profil pre takúto zmenu vyžaduje zameraný audit a čerstvé nezávislé overenie opravy.
- Nie je dôvod na automatický full-repository R4 audit.
- Nie je dôvod na E4: tento slice nemení produkciu, neničí dáta, nerotuje skutočné credentials ani nevykonáva migráciu.

Ak by sa realizovali iba pôvodné testy bez runtime opráv, E3 by nebolo primerané. Taký test-only variant by však **nevyriešil zistené nedostatky** a nie je odporúčaným uzavretím Slice 1.

### Rollout a rollback

Tento grant končí overeným lokálnym candidate a reportom. Neobsahuje deployment ani restart.

- Backendové zmeny nemenia DB schema.
- Frontendové tokeny zachovávajú existujúci persisted formát.
- Nie je potrebný data backfill.
- Rollback kódu nevyžaduje databázový rollback.
- Návrat na starý frontend by zároveň obnovil pomenované refresh race; to treba uviesť pri prípadnom neskoršom rollout rozhodnutí.

### Cooperator-owned rozhodnutia a odložené položky

V technickom návrhu nezostáva otvorené produktové rozhodnutie. Zachované sú už prijaté pravidlá vrátane GET-any-staff a HSTS preload residual. Finálne odovzdanie v chate bolo výslovne prijaté.

| Položka | Odloženie |
|---|---|
| PostgreSQL SQL kompatibilita a skutočná súbežnosť row locks | Slice 2; SQLite sondy túto vlastnosť nedokazujú. |
| Prevádzkové throttle enforcement, proxy trust, globálne headers | Slice 3; simulation scopes sú už naviazané. |
| VPS hardening, služby, host scripts, firewall a restarty | Slice 4; mimo repo-local aplikačného grantu. |
| Next.js standalone, packaging a build/deployment dôkazy | Slice 5. |
| `SECURE_HSTS_PRELOAD=True` | Mimo tohto plánu; prijatý residual sa neotvára. |
| Cross-tab refresh koordinácia alebo presun JWT do cookies | Samostatná session architecture zmena; tento slice rieši preukázané chyby jedného runtime. |
| Sprístupnenie diagnostic targets v playground | Nie je súčasťou prijatého produktu tohto slice. |
| Legacy reconstruction a dual-rack inference | Zakázané podľa A4. |

### Orchestration critique

**MEASURED**

- Hypotézy o základnom staff gate, read-only `is_staff`, existujúcom refresh Promise a staff B GET politike sa potvrdili.
- Pôvodná hypotéza „mutex už existuje, pravdepodobne stačia testy“ nepostačuje pre celý token lifecycle: syntetická sonda preukázala obnovenie auth po logout a prepísanie novej identity.
- Pôvodné vyhľadávanie nemenovalo všetky simulation ID error vetvy. Pri priamom overení vracali pomenované 500.
- Existujúci proxy test mockuje export odlišný od skutočne importovaného `POST`; dve existujúce vetvy nedokazujú LLM delegovanie.
- Vyhľadávanie názvov credentials iba v troch serializer/analytics súboroch nezachytí voľný vnorený obsah `ai_trace`.
- Výstupné kopírovanie rizikového JSON je doložené; produkčný únik skutočného credential doložený nie je.
- Archivačný konflikt bol odstránený výslovnou zmenou odovzdávacieho kontraktu.

**LEAD**

- Najvyššiu prioritu v implementačnom poradí má regresný test a oprava refreshu po zmene relácie.
- Creator policy sa má uzavrieť dôkazmi, nie novým modelom oprávnení.
- Na izoláciu Next.js requestov musí test použiť skutočný `AsyncLocalStorage`.
- Fresh audit má kontrolovať najmä vlastníctvo auth flight, úspešný aj neúspešný výsledok starej relácie, Django object ownership a hranice výstupných payloadov.
- PostgreSQL concurrency a produkčné throttle správanie nesmú byť deklarované ako overené na základe tohto reportu.

### Enumeration widened

Prieskum bol oproti pôvodným hypotézam rozšírený cielene:

- `rg --files` a vyhľadávanie `token|JWT|password` našli skutočný `test_token_lifecycle.py` a auth implementáciu.
- Vyhľadávanie `lease`, `simulation` a route testov viedlo k `test_simulation_services.py`, skutočnému turn route testu a simulation runneru.
- Vyhľadávanie `ai_trace|earlier_attempt_failures|sanitize|redact` viedlo k diagnostickým modelom, `_persist_ply`, existujúcim sanitizerom a frontend replay parseru.
- Vyhľadávanie importov provider runtime modulov a `NEXT_PUBLIC_` bolo rozšírené o Next config a bezpečný env template.
- Importy proxy viedli k `admin-simulation-server.ts` a `ai-move-execution.ts`.
- Vyhľadávanie `lexicon_source` viedlo k `game/inspection.py`; lexikonové IDs používajú názvy bez lokálnej cesty a verejný provenance zdroj.
- Konfigurácia testov bola prečítaná pred ich vykonaním, aby sa zabránilo načítaniu `.env`, kontaktu s existujúcou DB a zápisu pytest cache.
- Boli prečítané lokálne docs nainštalovaného Next.js pre route handlers a hranicu server/client environment; nebola použitá sieť.

```text
Report justification: new-evidence

Authority expiry:
Planning authority expires at this report.
No implementation authority is granted by this plan.

Smallest next step:
ORCHESTRATOR issues a fresh-worker-session implementation prompt with
Native planning mode: not-used, this frozen plan, the exact allowlist,
the isolated verification route, and E3/R3 acceptance requirements.

Context pressure:
Stredný; rozhodujúce tvrdenia sú podložené konkrétnym kódom, testami
alebo označenými izolovanými sondami.
```
