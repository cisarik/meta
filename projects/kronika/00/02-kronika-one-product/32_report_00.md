
```markdown
# S6: súkromné záznamy, prístup a administrátorské schvaľovanie

## 1. Výsledok a hranice

Implementovať S6 v `/home/agile/Projects/framenest` na vetve `feat/kronika-one-product`, proti baseline `40e51cb2d061ead96850c9c94aa59de54d5e1310` a AP pinu `7478ddb07d2c3911f79e1aa1441f0115a31c45d8`.

Výsledkom budú spoločné záznamy, nemenné dokončené Q/A dokumenty, jednotná autorizácia, schvaľovanie a odvolanie schválenia, súkromné databázové úložisko a vykonateľný inventár prístupových ciest.

Návrh nadväzuje na [dodaný report](/home/agile/.codex/attachments/b65d77d5-76ad-4ca3-ae40-6980fc468314/pasted-text.txt). Zachováva jeho návrh dokumentov, základných záznamov a transakcií; nižšie nahrádza otvorené G1–G3 a spresňuje schválenú projekciu.

Zostáva mimo S6:

- Migrácia 0035, poskytovatelia, účtovanie a vykonávanie Search/Research.
- Automatické vytváranie spoločných záznamov v reálnych importných tokoch, spoločné dokončenie požiadaviek, nové history/Timeline HTTP API a rendering zo S7-P.
- UI, historický backfill, živé databázy, reset, nasadenie a publikovanie.

Overený pracovný strom je čistý. Táto fáza nemenila súbory a nespúšťala testy. Aktuálny verejný remote nebol overovaný.

## 2. Dátový model, rozhrania a schválená projekcia — G2

### Záznamy a schvaľovanie

Použiť migráciu `0034_kronika_records.py`, SQLAlchemy Core a existujúcu databázu. Zachovať detailné stĺpce a obmedzenia `kronika_documents` a `kronika_records` z §3 reportu:

- UUID záznamov a dokumentov; `operation_id` zostáva ohraničený token.
- Jednoznačné väzby na médium, dokument a finálnu operáciu.
- Serverom odvodený vlastník, počiatočné `private`, oddelené časy vytvorenia, dokončenia a prvého vstupu do Timeline.
- Žiadna automatická konverzia starých publikácií ani priradenie vlastníka historickým médiám.
- Žiadne aplikačné operácie meniace vlastníka alebo dokončený Q/A dokument.

Aplikačný port poskytne vytvorenie dokončeného dokumentu so záznamom, čítanie detailu, vlastnú históriu, administrátorský inventár, schválený Timeline, prípravu kandidáta, schválenie a odvolanie. Vstupom bude validovaný serverový kontext, nie klientom zvolený vlastník.

Schválenie a odvolanie vykonať v `BEGIN IMMEDIATE`. Schválenie vyžaduje administrátora, očakávanú verziu, validované dokončenie a pri médiách úspešnú analýzu spolu s uloženým titulkom, popisom a tagmi. Kandidát obsahuje verziu, analýzu a digest celej schvaľovanej projekcie; transakcia všetko znovu porovná.

Zachovať pravidlá opakovania z §4.3 reportu: starý token je konflikt; presné opakovanie s aktuálnym tokenom môže byť bez zmeny. Odvolanie zachová dokument, schválenú projekciu a prvý čas vstupu do Timeline. Opätovné schválenie nemení poradie karty.

### Projekcia musí riadiť aj SQL

Samotný `approved_projection_json` nestačí na bezpečné filtrovanie. Migrácia preto pridá tri relačné tabuľky:

| Tabuľka | Obsah |
|---|---|
| `kronika_approved_media` | Jeden riadok na schválený mediálny záznam; verzia schválenia a zmrazené skalárne polia súčasného katalógového modelu vrátane klasifikácie, autora a digestu obalu. |
| `kronika_approved_media_tags` | Kľúč tagu, schválený zobrazovaný názov a poradie; bez čítania aktuálneho názvu pri zobrazovaní snímky. |
| `kronika_approved_media_locations` | Schválené identifikátory umiestnení a ich uložené charakteristiky potrebné na výber podporovaného média a kontrolu zdroja. |

Použiť existujúce typy a doménové obmedzenia príslušných polí. Tabuľky majú väzbu na spoločný záznam; umiestnenia majú kontrolovanú väzbu na fyzické umiestnenie. Ich výmena prebieha atomicky so schválením.

Verziovaný JSON zostane úplnou normalizovanou snímkou pre detail: metadáta vrátane žánrov, schválený výsledok analýzy, obal a umiestnenia. Relačné polia sa vytvoria z tej istej validovanej hodnoty. Nepotrebuje sa SQLite JSON rozšírenie.

Zaviesť typovaný rozsah čítania a rozhodnutie obsahujúce `deny`, `current`, `approved` alebo `legacy`. Chýbajúci rozsah odmieta prístup. `legacy-public` bude samostatný interný rozsah dostupný iba verejnej kompozícii.

| Povrch | Výsledné správanie |
|---|---|
| Gallery, detail a companion picker | Vlastník a administrátor čítajú aktuálny pracovný stav; ostatní členovia iba schválenú snímku. |
| Vyhľadávanie, kategórie, tagy, počty, stránkovanie | Najprv zostaviť autorizovaný SQL výber aktuálnych alebo schválených riadkov, až potom filtrovať a počítať. |
| Workspace a companion own-history | Vlastníctvo spoločného záznamu má prednosť; príspevkové väzby platia iba pre nezviazané historické médiá. |
| Metadáta a analýzy | Pri `approved` serializovať snímku; nevolať službu vracajúcu najnovší súkromný výsledok. |
| AI suggestions | Členovi domácnosti vrátiť iba schválený výsledok, bez kurzora do aktuálnej histórie analýz. |
| Movie identification | Vrátiť schválený výsledok príslušného typu; ak v snímke nie je, použiť existujúcu reprezentáciu neprítomného výsledku. |
| Aliasy | Zachovať osobný overlay volajúceho; prístup k médiu overiť pred čítaním aj zápisom aliasu. |
| Obal | Použiť schválený digest existujúceho nemenného artefaktu aj pre ETag. Chýbajúci artefakt nenahrádzať aktuálnym obalom. |
| Originál, download a preview | Overiť médium, schválené umiestnenie a zhodu zdroja pred otvorením alebo použitím cache. Nové neschválené umiestnenie ani zmenený zdroj nesmú poslúžiť ako náhrada. |
| Verejná kompozícia | Vylúčiť všetky spoločné záznamy vrátane `family`, aj pri chybnom starom publikačnom riadku. |

Existujúce zapisovače metadát, companion review a obalu zvýšia verziu **už zviazaného** záznamu pri skutočnej zmene, v rovnakej transakcii. `record_analyzed` aktualizuje jeho poslednú úspešnú analýzu po validácii výsledku; pending/failed beh nemení predchádzajúci úspech ani schválenú snímku. Tieto podmienené aktualizácie patria do S6, pretože chránia jeho schvaľovacie pravidlá. Vytváranie väzieb v reálnom ingestovaní zostáva S7-P.

Starý publish/unpublish aj odstránenie média odmietnu zviazaný záznam typovaným konfliktom. Kontrola musí byť v zapisovacej transakcii pred vložením potvrdenia o odstránení, odpojením väzieb alebo následným mazaním súborov.

## 3. Identita, upload a acquisition — G1

### Explicitný lokálny vlastník

Pridať voliteľné nastavenie `local_owner_login`, dostupné cez `FRAMENEST_LOCAL_OWNER_LOGIN`. Hodnotu normalizovať existujúcou funkciou a vyžadovať jej prítomnosť v `identity_map`. Rolu a schopnosti prevziať z mapovania; neprideľovať administrátora automaticky.

Lokálny adaptér vytvorí identitu s osobitným pôvodom `local-config`:

- Iba pre skutočný loopback TCP prístup a existujúci lokálny operator kanál workspace UDS.
- Nikdy pre verejnú kompozíciu ani ako náhradu neplatnej alebo nemapovanej vzdialenej identity.
- Klientské identity a proxy hlavičky nesmú vybrať lokálneho vlastníka.
- Pri nakonfigurovanej identite uplatniť existujúce schopnosti trás a audit privilegovaných mutácií.
- Lokálne browser mutácie kontrolujú presný nakonfigurovaný loopback origin; operator API naďalej odmieta `Origin`.
- Bez konfigurácie zostáva obsah nedostupný; zdravie služby a statické zdroje nevyžadujú identitu.

### Uzavretie prístupových ciest

| Povrch | Zmena |
|---|---|
| Upload create/capability | Vyžadovať platnú identitu a upload capability pred volaním transportu; vytvorenie uloží jej login. |
| Upload GET/PATCH/DELETE/complete/duplicate-resolution | Chýbajúca identita odmieta; cudzia a neexistujúca session majú rovnakú odpoveď. Staré session bez vlastníka sú dostupné iba administrátorovi. |
| Upload duplicity | Bežnému používateľovi ponechať `SILENT_KEEP_SEPARATE`; neodhalovať cudzie ID, titulok, hash ani rozdiel podľa súkromnej zhody. Administrátor môže používať explicitné riešenie. |
| Upload `media_id` | Pred serializáciou samostatne autorizovať naviazané médium. Oprávnenie na upload session samo osebe nestačí. |
| YouTube requester | Vlastníctvo requestu riadi jeho históriu; čitateľnosť média riadi spoločná politika. Zakázaný odkaz vráti `media_id=null` a existujúcu fázu `unavailable`. |
| YouTube opätovné použitie | Kandidáta vybrať s autorizačným SQL pred `LIMIT`. Starý publikačný riadok nesmie sprístupniť zviazané súkromné médium. |
| X requester | Zachovať vlastné requesty a ich priebeh; zakázané mediálne odkazy v assets zneprístupniť. Pred opätovným použitím, čítaním živej kategórie a aplikovaním aliasu overiť naviazané médium. |
| Administrátorské acquisition API | Zachovať explicitné schopnosti, audit a read-all; žiadna autorita odvodená iba zo sieťového členstva. |
| Lokálny YouTube operator | Vyžadovať nakonfigurovanú identitu s acquisition capability a odovzdať ju službe; samotný loopback už nestačí. |
| Analysis proposals | Overiť objekt aj v transakcii pred vložením návrhu; zachovať rate limits a audit. |

Interné recovery/coordinator operácie nezískajú umelú administrátorskú identitu. Použijú uloženú provenienciu pôvodnej operácie; ich interné snapshoty sa nesmú priamo serializovať requesterovi bez autorizačnej projekcie.

Inventár musí používať skutočné trasy. Opraviť najmä návrhové označenia acquisition trás na existujúce `/api/admin/youtube/claims`, `/api/operator/youtube/claims` a `/api/admin/x/requests/{claim_id}`.

## 4. Súkromný stav — G3 a hranice súborových zmien

### Databázový životný cyklus

Pridať spoločný POSIX helper pre vytváranie a kontrolu súkromného katalógu:

- Nový databázový adresár vytvoriť ako `0700`, nový databázový súbor ako `0600`, bezpečne a bez prepísania existujúceho objektu.
- Existujúci adresár, DB, WAL, SHM a rollback journal overiť na typ, vlastníka a oprávnenia. Odmietnuť symlink na chránenom objekte a viacnásobný hardlink databázového súboru.
- Nevyhovujúce existujúce objekty odmietnuť bez `chmod`; nemenia sa nadradené systémové adresáre.
- Zachovať lenivé vytvorenie SQLAlchemy engine: príprava prebehne pri otvorení spojenia, nie pri importe či konštrukcii engine.
- Kontrolu použiť pre zapisovacie aj read-only spojenia, migrácie, vývojový launcher a backup/restore vstup či cieľ katalógu. Read-only cesta nič nevytvára.
- Súkromný adresár chráni aj vznikajúce SQLite pomocné súbory; ich režimy overovať pri otvorení a transakčných hraniciach. Nemení sa globálny procesový `umask` aplikácie.
- Na nepodporovanej platforme odmietnuť otvorenie so sanitizovanou chybou. Windows ACL nie sú súčasťou S6.
- Chyby a logy nesmú obsahovať dokumenty, SQL parametre ani obsah súkromného stavu.

Upgrade zachová staré riadky a vytvorí nula spoločných záznamov. Downgrade povoliť iba pri prázdnych nových tabuľkách; inak odmietnuť pred DDL. Backup/restore musí zachovať všetky nové tabuľky a súkromné oprávnenia.

### Uzavretý katalóg zmien

Základ tvoria presné množiny **N, P, T a H** v §5, §7 a §8 dodaného reportu. Dopĺňajú sa nasledujúce cesty; nejde o povolenie upravovať celé adresáre. Mená v každom riadku sa pripájajú k uvedenému prefixu.

| Prefix | Doplnené produkčné súbory |
|---|---|
| `src/framenest/` | `configuration.py` |
| `src/framenest/domain/` | `identity_access.py` |
| `src/framenest/adapters/api/` | nový `local_identity_api.py`; `tailscale_ingress.py`, `upload_api.py`, `youtube_request_api.py`, `youtube_browser_api.py`, `youtube_operator_api.py`, `x_request_api.py`, `x_companion_api.py`, `workspace_media_api.py`, `companion_review_api.py`, `media_metadata_api.py`, `media_alias_api.py`, `media_analysis_lifecycle_api.py`, `media_suggestion_api.py`, `media_content_api.py`, `gallery_preview_api.py`, `cover_api.py`, `catalog_removal_api.py` |
| `src/framenest/application/` | `youtube_acquisition.py`, `x_acquisition.py`, `workspace_media.py`, `companion_review.py`, `media_cover.py`, `media_content.py`, `gallery_preview.py`, `catalog_removal.py` |
| `src/framenest/application/ports/` | `youtube_acquisition_claims.py`, `x_acquisition.py`, `companion_review_repository.py` |
| `src/framenest/infrastructure/persistence/` | nový `private_state.py`; `engine.py`, `migrations.py`, `catalog_backup.py`, `youtube_acquisition_claim_repository.py`, `x_acquisition_claim_repository.py`, `media_analysis_run_repository.py`, `media_cover_repository.py`, `catalog_removal_repository.py` |
| `src/framenest/infrastructure/runtime/` | `development.py` |
| Koreň a dokumentácia | `SECURITY.md`, `DEVELOPMENT.md`, `docs/BACKUP_AND_RECOVERY.md` |

`upload_catalog.py`, `upload_publication_repository.py` a `media_repository.py` sa v S6 nemenia na vytváranie spoločných záznamov. Transakčný helper z nového record repository sa overí synteticky; zapojenie do reálneho ingestovania zostáva S7-P.

Doplnené testové cesty:

| Prefix | Súbory |
|---|---|
| `tests/` | nový `conftest.py` iba pre súkromné oprávnenia syntetických fixture súborov; žiadna globálna identita ani permissive policy |
| `tests/contract/` | nové `test_local_record_identity.py`, `test_kronika_acquisition_authorization.py`, `test_kronika_approved_projection.py`; `test_upload_api.py`, `test_ordinary_upload_ownership_boundary.py`, `test_youtube_request_api.py`, `test_requester_private_youtube_details.py`, `test_youtube_operator_api.py`, `test_youtube_browser_api.py`, `test_x_request_api.py`, `test_x_companion_api.py`, `test_workspace_media.py`, `test_public_published_uds.py`, `test_tailscale_ingress_security.py`, `test_content_publication_api.py`, `test_content_publication_unpublish.py`, `test_catalog_removal_api.py`, `test_media_metadata_repository.py`, `test_cover_ingress.py`, `test_atomic_upload_publication_contract.py` |
| `tests/integration/` | `test_local_web_upload_cockpit.py`, `test_atomic_upload_publication.py`, `test_youtube_acquisition_lifecycle.py`, `test_local_web_media_catalog.py`, `test_local_web_media_metadata.py`, `test_local_web_media_metadata_workspace.py`, `test_still_image_vertical_slice.py`, `test_still_image_cover_slice.py`, `test_cover_workflow_real_tools.py`, `test_development_launcher.py` |
| `tests/integration/persistence/` | `test_catalog_removal_repository.py`, `test_content_publication_repository.py`, `test_media_cover_repository.py` |
| `tests/unit/` | `test_identity_access.py`, `test_configuration.py`, `test_configuration_ingress.py`, `test_persistence_engine.py`, `test_companion_picker.py` |
| `tests/unit/application/` | `test_list_workspace_media.py`, `test_companion_review.py`, `test_media_cover.py`, `test_media_content_application.py`, `test_x_acquisition_lifecycle.py`, `test_youtube_catalog_title_import.py`, `test_creator_catalog_filter.py` |
| `tests/unit/infrastructure/persistence/` | nový `test_private_state.py`; `test_media_analysis_run_repository.py`, `test_companion_review_repository.py`, `test_engine_readonly_uri.py` |
| `tests/unit/infrastructure/runtime/` | `test_development_runtime.py` |

Existujúce pozitívne HTTP fixtures dostanú explicitného syntetického volajúceho alebo nakonfigurovaného lokálneho vlastníka. Izolované testy môžu používať politiku obmedzenú na konkrétne fixture ID. Autorizačné dôkazy musia používať skutočnú politiku a SQLite.

## 5. Implementačné poradie a prijatie

Postupovať v jednom S6 implementačnom zadaní:

1. Overiť baseline, vetvu, čistotu, AP pin a voľnú revíziu 0034.
2. Implementovať súkromné otvorenie databázy, migráciu, doménu a transakčné služby.
3. Zapojiť typovaný prístup, lokálnu identitu, acquisition kontroly a schválené projekcie.
4. Doplniť inventár, testy a pravdivé stavové dokumenty.
5. Po úspešných kontrolách vytvoriť jeden lokálny commit; nasleduje samostatná nezávislá E3/R3 kontrola konkrétneho SHA.

Povinné scenáre:

- Alice: vlastné súkromné a nedokončené záznamy; Bob: odmietnutie; administrátor: read-all; člen: schválená snímka; anonymná a verejná kompozícia: odmietnutie.
- Falošná identita, klientský vlastník, chýbajúca politika, neplatná lokálna konfigurácia a zlyhanie auditu.
- Rovnaké odpovede pre cudzie a neexistujúce objekty; žiadne downstream otvorenie súboru, poskytovateľ ani zápis pri odmietnutí.
- Súkromná duplicita bez úniku; konfliktné legacy contribution/publication väzby; zakázané mediálne odkazy v upload/YouTube/X odpovediach.
- Schváliť A, zmeniť pracovný stav na B: člen stále vidí A v detaile, filtroch, počtoch, analýze a obale. Po opätovnom schválení vidí B na rovnakej pozícii Timeline.
- Súbežné schválenie/odvolanie, zastaraný digest, zmena metadát či obalu, neúspešná analýza a rollback bez čiastočného výsledku.
- Zviazané médium nemožno odstrániť starou cestou; nevznikne receipt ani cleanup.
- Nové a existujúce bezpečné/nebezpečné DB objekty, symlinky, hardlinky, WAL/SHM/journal, read-only režim, nepodporovaná platforma a sanitizácia logov. Bezpečnú tvorbu testovať aj pri `umask 022`.
- Upgrade naplneného syntetického 0033, všetky FK/CHECK/UNIQUE obmedzenia, prázdny downgrade a odmietnutie naplneného downgrade; backup/restore s dokumentmi a projekciami.
- Inventár porovnať so skutočnými metódami oboch aplikácií a workspace route policies. Každá obsahová cesta musí odkazovať na pozitívny aj negatívny behaviorálny test.

Testy spúšťať výhradne cez deklarované `./.ap/ap project check` a `./.ap/ap exec --operation test-focus`, vždy s uvedeným baseline. Najprv nové a dotknuté testy; následne raz `tests/unit tests/contract tests/integration -q -p no:cacheprovider`, pretože zmena zasahuje zostavovanie aplikácie aj databázový engine. Bez živých poskytovateľov, browsera či hostových operácií.

Zmena mimo uzavretého katalógu, nevysvetlený neúspech alebo odchýlka baseline zastaví implementáciu na konkrétnom probléme. Lokálny commit bude mať predmet `feat(kronika): add private records and administrator approval`; push ani nasadenie nie sú súčasťou zadania.

Prijatie S6 vyžaduje úspešné testy, úplný inventár, transakčné dôkazy a samostatnú čerstvú autorizačnú kontrolu. Tento plán nepredstavuje Implementation PASS ani povolenie vykonať implementáciu.
```

