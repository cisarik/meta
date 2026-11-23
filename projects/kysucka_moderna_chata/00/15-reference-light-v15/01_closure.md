# 01_closure — V15 · svetlo a obloha chaty v údolí

**CELOK UZAVRETÝ ORCHESTRÁTOROM**

**19. 11. 2026 · Orchestrátorka celku · `kysucka-moderna-chata-reference-light-v15`**

Technická iterácia V15 je dokončená. Vizuálny výsledok je **PARTIAL**. Ako východisko pre ďalšie vizuálne posúdenie som vybrala **C**. Výber finálneho svetla patrí Michalovi.

## Obnova a porovnanie

Po výpadku elektriny som obnovila prácu z uloženého checkpointu V14 s overeným SHA-256. Varianty B a C vznikli v izolovanom Blenderi mimo Michalovho otvoreného súboru. V15 upravila svetlo a oblohu. Kontroly po uložení a opätovnom otvorení potvrdili zachovanie chaty, interiéru, vegetácie, terénu, materiálov a kamery. C šiestimi hodnotami upravila intenzitu a farbu výplne, oblakov a hlavného slnka.

| Záber | Čo vidno | Čas renderu |
|---|---|---:|
| [A · V14](/home/agile/Projects/kysucka_moderna_chata/work/v14/native_02/renders/B_final960.png) | Dlhé tiene a chladnejšie, tmavšie popredie. | 106,14 s |
| [B · V15](/home/agile/Projects/kysucka_moderna_chata/work/v15/reference_01/renders/B_reference960.png) | Kratší tieň chaty, čitateľnejšie oblaky a svetlejšia lúka s menším farebným kontrastom. | 105,23 s |
| [C · V15](/home/agile/Projects/kysucka_moderna_chata/work/v15/reference_01/renders/C_tonal960.png) | Teplejšie oblaky, tmavšia výplň lúky a čitateľnejšie bočné svetlo na chate. V tieni stromov ubudol detail. | 104,13 s |

Všetky tri PNG majú 960 × 540. Záznamy potvrdili zhodnú kameru `CAM_V11_VALLEY_REVIEW` vrátane polohy a optiky, Cycles CPU so 4 vláknami, 96 vzoriek, OIDN Accurate/High a AgX/None. C sa úplne dekódoval. Render C dosiahol špičku 4,27 GiB RAM procesu a minimum dostupnej systémovej RAM bolo 17,55 GiB.

K dispozícii je [natívny 4K render V14](/home/agile/Projects/kysucka_moderna_chata/work/v14/delivery_02/renders/chata_v14_4k.png) v 3840 × 2160. Dokončil sa za 19 min 15 s, so špičkou 6,12 GiB RAM procesu. B a C sú výstupy na výber svetla v 960 × 540.

## Otvorené body

- Oproti [Michalovej referencii 01.png](/home/agile/Projects/chata/chatgpt/01.png) ostáva lúka hladšia a zlaté akcenty na svahoch slabšie. Na rýchly výber stačí porovnať B a C. B ukazuje viac detailu v tieni, C má teplejšie svetlo a výraznejšie tiene pri chate.
- Použiteľnosť pracovného zobrazenia máme zmeranú na V14 pri 1440 × 900. Solid dosiahol 30,79 FPS za celý oblet. Material Preview dosiahol 12,45 FPS na 40° úseku, úvodné prekreslenie trvalo až 508 ms a vonkajší terén bol neprirodzene svetlý.
- Nepravidelná šírka krajníc z V07 ostáva odložená. Úprava patrí do samostatného kroku pri ďalšej práci na chodníku.

## Identita a uzavretie

| Lokálny artefakt | SHA-256 |
|---|---|
| [V14 · východisková scéna](/home/agile/Projects/kysucka_moderna_chata/work/v14/native_02/checkpoints/candidate_exterior_v14.blend) | `1e9f5fa2a6bd07db01e3218a0503de3b64a846f407d2b7661ba3e4bb94d6b6b2` |
| [V15 B · scéna](/home/agile/Projects/kysucka_moderna_chata/work/v15/reference_01/checkpoints/candidate_exterior_v15.blend) | `dccb4a1886a6f7c6ff2be6ec84aa21a787dcba172a49d34bbf125a03958a2126` |
| [V15 C · vybraný kandidát na posúdenie](/home/agile/Projects/kysucka_moderna_chata/work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend) | `15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2` |
| V15 C · PNG | `3110941602665c563dfbe9bfe4ce9f118fb4d11dcb2fbc14ffeff15b3b8704d2` |
| V14 · 4K PNG | `badca818d6c037062af65289587f23cf77ac940dacc5e58bcc6cfb0160cc4e0c` |

Podklady k výsledku tvoria záznamy o zhodnom nastavení, kontroly uložených scén a priame porovnanie výstupov. Zdrojové postupy aj protokoly sú v `work/v15/reference_01/`. [V15 B · report 02/01](/home/agile/Projects/kysucka_moderna_chata/work/v15/reference_01/report_01.md) · [V15 C · report 02/02](/home/agile/Projects/kysucka_moderna_chata/work/v15/reference_01/report_02.md) · [V14 · report 4K a obletu](/home/agile/Projects/kysucka_moderna_chata/work/v14/delivery_02/report_01.md)

```text
Phase-qualified result: implementation-PASS
Result artifact or commit: lokálny kandidát V15 C s identitou uvedenou vyššie
Result evidence: zhodné A/B/C, kontroly po opätovnom otvorení, dekódované PNG, reporty 02/01 a 02/02
Required preceding results: satisfied pre technickú iteráciu V15
Cooperator-owned decisions: satisfied pre technické uzavretie na žiadosť Michala. Vizuálny výber je samostatný
Residual-risk disposition: satisfied. Otvorené body sú uvedené vyššie
Upgrade-ledger reconciliation: complete. Projekt nemá deklarovaný register aktualizácií AP
Active-context reconciliation: complete
Active mutation: none v rozsahu V15. Oprávnenia Workera skončili a render nebeží
Closure authority: present
Audit completion: technická kontrola dôkazov dokončená
Orchestrator acceptance: potvrdené technické dôkazy
Publication: mimo rozsahu
Public Git equality: not-applicable
Closure actor: ORCHESTRATOR
Logical-whole closure: closed-by-ORCHESTRATOR
```

Checkpointy a obrázky v `work/` sú lokálne pracovné výstupy. Projekt je na `78534bd46020bb2bfc97eef69b05e583cba5a5e5` s AP pinom `d7023cf037f6d17885c3ede5c04812c61640da50`. Zápis do Meta je lokálny. Stav vizuálneho prijatia a publikovania V15 ostáva otvorený.
