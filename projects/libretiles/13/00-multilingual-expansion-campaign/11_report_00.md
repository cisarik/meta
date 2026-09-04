> ⚠ **ORCHESTRATOR ARCHIVAL NOTE, mine and not the Worker's.** Archived verbatim, condensed only by
> omitting nothing. Status `PASS`; `frontend/src/lib/i18n/messages.pt.ts` landed as `dd3b176`, pushed,
> readback equal, porcelain clean. **ACCEPTED.** Its `Orchestration critique` found the **EIGHTH**
> defect in the `[INVARIANT]` skeleton and it is the sharpest one yet: section 7.1's ` as ` grep
> collides with the TARGET LANGUAGE rather than with the header, and the prompt's own wording then
> instructed the Worker to damage correct Portuguese. Verified by me: five hits, all feminine plural
> definite articles inside correct string values; the cast-shaped replacement returns zero. My rulings
> on all eleven of its findings are in `./00_notes.md` §43. The full report as returned follows.

### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: multilingual-expansion-campaign
Worker session ordinal: 11, Worker exchange ordinal: 01
```

**Status:** PASS
**Phase-qualified result:** Implementation complete — MEC-UIL-C2-pt, the European Portuguese interface catalog, catalog 2 of 8.
**Start commit:** `74e9d369e5a4a3054fd149a7d270a9b1fd40112c`
**End commit:** `dd3b1764144d1a9db8b8183f4556763440499bdf`

**Changed files and purpose**
`frontend/src/lib/i18n/messages.pt.ts` (NEW, only path, 440 lines) — 296 `ptText` keys and 20 `ptFn` keys in `messages.en.ts` key order. Deliberately orphaned: `LOCALES` untouched at four, nothing imports it. No existing file modified, moved or deleted.

**Tests and validation**
Repository gate: all seven values matched (HEAD, `HEAD:.ap` = `9c5cc44f8b6c92dd56ad2427d13223d7d59c5656`, detached `.ap` HEAD identical, `## main...origin/main`, empty porcelain, remote at baseline, no listener on 3000/8000).

Structural audit (7.1): one `?? ` line before staging; `head -7` byte-diff against `messages.de.ts` EMPTY; `grep -c 'pluralPt('` = 3; `grep -c 'plural'` = 4 (one import, three calls, nothing else); zero `aria-live` / `role="status"`; `git diff --check` clean; 296 + 20 keys; UTF-8 accents intact; zero empty values. The type-weakening grep returned **5 hits, none of them a weakening** — see MEASURED #1.

Four frontend gates, all green:
- `npm run typecheck` — exit 0, zero diagnostics. **The code type-checks.**
- `npx vitest run` — 467 passed / 3 skipped, 32 files passed / 1 skipped. I measured that same baseline *before* creating the file, so "unchanged" is measured rather than assumed.
- `npm run lint` — clean.
- `npm run build` — exit 0, "Compiled successfully". **The build passed**, and separately: eleven dynamic routes, zero static.

Backend five not run: diff confined to `frontend/`, pytest collects only `backend/`, mypy scope is `config game gamecore accounts catalog`. Explicit recorded deviation.

**Commit and push**
One non-force commit `dd3b176` (1 file, 440 insertions, `create mode`), staged with the exact single path. Pre-push gate: `HEAD~1` = `74e9d369…` and remote still `74e9d369…`. One `git push origin main`: `74e9d36..dd3b176`. Readback: local HEAD == remote main == `dd3b1764144d1a9db8b8183f4556763440499bdf`. Working tree clean, `.ap` gitlink unchanged.

**Deviations, risks, missing evidence**
One deviation (backend gates, above). Missing evidence: rendered acceptance — the file renders nowhere, and that owner is the Cooperator after the wiring slice. My evidence is not independent.

**Resolved Execution Issues / Near-Misses:** none.
**Pre-Existing Failure Classification:** none.

---

### Terminology and choices

Nine frozen terms (canonical home is the file's terminology block):

| concept | pt-PT |
|---|---|
| tile | peça |
| letter | letra |
| rack | suporte |
| blank | peça em branco |
| bag | saco |
| board — playing surface | tabuleiro |
| board — a saved game | partida |
| pass | passar (noun `passe`); exchange is `trocar`, a different word |
| points | pontos (PTS / pts) |
| rival = opponent | adversário (one word for both) |

**Register:** informal `tu` everywhere, error messages included. Zero `você`, zero formal forms.

**Label style:** infinitive for every control, action label, column heading and accessible name; `tu` imperative only for prose sentences and hero headings. One documented exception, commented in the file: `history.prev` / `history.next` are ordinals (`Anterior` / `Seguinte`), because Portuguese pagination is not a verb pair.

**pt-PT computing vocabulary (5.2 item 5):** utilizador / nome de utilizador · palavra-passe · iniciar sessão, terminar sessão · registo, Registar · definições · guardar, guardada, retomar · arrastar e largar · atualizar · fila · sala. Reinforced by ligação (not conexão), predefinido (not padrão), pesquisa (not busca), em direto (not ao vivo), partilham (not compartilham), aspeto (not aspecto). Measured: zero pt-BR sentinels in any string value; the only occurrences are the rejected forms named inside the terminology comment.

**Progressive aspect:** `estar a` + infinitive at every site — `game.status.opponentPlaying` "está a jogar", `game.status.aiThinking` "A AI está a pensar", plus `A iniciar sessão…`, `A preparar a partida…`, `A entrar na fila…`, `A sair da fila…`, `A desistir…`, `A terminar sessão…`, `A alterar…`, `A começar…`, `A carregar partidas…`, `A tirar peças do saco…`, `A procurar jogadas…`, `A filtrar…`, `A mostrar …`. Measured: zero gerunds; the single `-ndo` token in the file is `quando`.

**Nine counted-noun forms**, three slots × three sites, `pluralPt` called with four arguments each time:

| site | one (INCLUDES ZERO) | other | many |
|---|---|---|---|
| `a11y.rackTile` | ponto | pontos | pontos |
| `error.throttled.minutes` | minuto | minutos | minutos |
| `controls.tilesSelected` | peça | peças | peças |

`many` repeats `other` at all three sites, per the prompt's recommendation — I did not depart from it. `controls.tilesSelected` uses the colon-label shape (`Seleção: {n} peça/peças`) so the slots stay pure nouns; the alternative, `{n} peça selecionada`, would have forced a four-way participle agreement into the slots. `game.toast.invalidWordHeading` branches on `p.count > 1` into two full forms with adjective agreement (`Palavra inválida!` / `Palavras inválidas!`), never a suffix trick. `history.showing`, `history.pageOf` and the three `overlay.stats.*` are noun-free or colon-labelled.

**Protected tokens — one translated, five kept.** `model` → `modelo` in `landing.card.ai.body` ("Partidas premium com escolha de modelo"): on a landing page it is an ordinary noun, `modelo` is unambiguous in Portuguese, and no control in this catalog is labelled "model" for the user to match against. `chat` kept English in all five of its sites (`landing.card.queue.body`, `a11y.chatInput`, `chat.title`, `chat.unavailable`, `game.toast.chatOffline`): there it names the product's chat panel, `chat` is ordinary everyday Portuguese computing vocabulary in Portugal, and `conversa` would break the match between the a11y name and the visible panel. `Libre Tiles`, `AI`, `Collins Scrabble Words 2019` and its word count preserved; `landing.footnote` uses `\u00A0` as written, per the sk/pl precedent.

---

### Flagged risks

**Labels I believe may overflow, kept correct rather than shortened**

1. `header.logout` "Terminar sessão" (15 chars vs English 6) and `header.loggingOut` "A terminar sessão..." (20) sit on `whitespace-nowrap shrink-0` pills in the non-wrapping ScorePanel header flex cluster (`ScorePanel.tsx:346`), alongside `header.giveUp`, `header.profile` and `header.games`. **The highest overflow risk in the catalog.** `Sair` would fit but is imprecise and would break the `Iniciar sessão` / `Terminar sessão` pair, so I kept the correct term.
2. `controls.confirmExchange` "Confirmar troca" — nowrap, `h-[2.65rem]` fixed height, half of a two-column mobile grid, rendered at `text-[1rem]`→`text-[1.42rem]` (`GameControls.tsx:47`). German shipped 17 chars here, so it is probably survivable, but it is not measured.
3. `board.pinchToZoom` "Zoom com dois dedos" + `board.dragToPan` "Arrastar para mover" + `board.hide` "Ocultar" all share the one `inline-flex max-w-full` pill at `text-[0.72rem] uppercase tracking-[0.18em]` (`Board.tsx:665-680`) that English already fills. 19 + 19 + 7 against 13 + 11 + 4.
4. `history.col.rival` "Adversário" and `history.col.updated` "Atualizada". **Correction to the prompt:** the history table headings are *not* width-constrained — `<table className="min-w-full">` with plain `<th className="px-4 py-3">`, no nowrap, no minima (`GameHistoryPanel.tsx:286-294`). Risk here is low; the ~5rem minima in 5.5 belong to ScorePanel's score-name columns, not this table.
5. `header.backToBoards` "Voltar às partidas" reaches only an `aria-label` and an absolutely-positioned `whitespace-nowrap` tooltip; the button itself is icon-only at `w-[3.08rem]`. No layout risk, viewport-edge clipping only.
6. `settings.steps.50` "Profundidade de pesquisa predefinida" (35 chars) in a `minmax(132px,1fr)` / `minmax(170px,1fr)` settings grid. It wraps rather than truncating, but it is the longest label I wrote.

**Strings I am genuinely unsure of**

7. `rack` → **suporte**. My weakest term. `estante` is the alternative I rejected as more Brazilian-flavoured; a Portugal Scrabble player may use a word I do not know. It propagates to `rack.empty`, `history.endReason.bagEmpty`, `settings.premium.description` and `game.toast.aiExchangedBody`.
8. `settings.gameVariant.dutch` → **Neerlandês**. The correct pt-PT glottonym, but `Holandês` is far more common colloquially in Portugal. A recognisability-versus-correctness call.
9. `settings.gameVariant.afrikaans` → **Afrikaans** kept unchanged (Portuguese has no settled exonym), and `game.lexicon.afrikaans` treats it as an invariable adjective: "no léxico afrikaans". Same reasoning German recorded, different mechanism.
10. `board.reset` → **Repor** (not `Reset`, not `Reiniciar`): shortest idiomatic pt-PT and a genuine Portugal tell, but it is a UI verb a reviewer might want as `Reiniciar`.
11. `history.outcome.gaveUp` "Desistência" versus `history.endReason.gaveUp` "Por desistência" — two keys, one root, deliberately different registers (a badge versus a reason phrase). Worth a reviewer's eye.
12. `game.toast.passRejected` "Passe rejeitado" derives a noun (`passe`) from the frozen verb (`passar`). Portuguese has no crisp deverbal noun here; `passe` is a sports borrowing.

**Places grammar or a fixed call site forced a construction English did not have**

13. `draw.reason.closer` — the runtime values are tile letters (confirmed at `frontend/src/lib/draw-result.ts:29-30`), and a bare letter's gender is not settled in Portuguese. I used the **invariable** "está mais perto de A do que" rather than the adjective "mais próxima", which would have been a guess. `draw.subtitle` keeps "a peça mais próxima de A" because there the feminine noun is explicit. Commented at the key.
14. `settings.board.active` → **"Em uso"**, not "Ativo"/"Ativa". The badge renders beside a surface name that is feminine (`Madeira`) or masculine (`Preto`, `Verde`) at `settings/page.tsx:218-220`, so no agreeing adjective is correct at all three. Phrased around, as instructed. Commented at the key.
15. `history.unknownDate` → **"Desconhecido"** (unmarked masculine), not "Desconhecida". **The key name is misleading:** it is also the fallback for a missing *username* at `ProfileModal.tsx:220`, so no form agrees at both sites. Splitting the key is outside my allowlist. Commented at the key.
16. The eight `history.outcome.*` values are nouns or invariable phrases (`À espera`, `Em curso`, `Vitória`, `Derrota`, `Empate`, `Desistência`, `Abandono`, `Desconhecido`) rather than adjectives, because the same badge is read against `partida` (f.) in one place and the `Resultado` (m.) column in another. Commented above the group.
17. `game.aiPlayedFor.before` / `.points` (`page.tsx:338`) — **no constraint for Portuguese**, unlike German. The score span is fixed in the middle, and Portuguese wants verb → number → noun, so "A AI marcou 42 pts" composes natively; the pretérito perfeito is one word before the object, so nothing had to be abandoned. Commented at the key.
18. `board.reset` + `board.zoomNoun` (`Board.tsx:692-693`) — **also no constraint for Portuguese**. The call site forces `[action][noun]`, which is exactly Portuguese order: "Repor zoom". Commented at the key.
19. `AI` takes feminine agreement throughout ("a AI", "A AI será declarada vencedora"), matching `a inteligência artificial`. A Portuguese reviewer will likely want the token itself to be `IA` — that is a protected-token change I am not authorised to make, so I recorded the constraint in the terminology block instead.
20. `draw.blankCaption` → "em branco", not the frozen "peça em branco": the caption renders directly under the peça it labels, in a `text-[0.7rem] tracking-[0.24em]` span (`draw/[id]/page.tsx:109-116`), where the noun is both redundant and far too wide. The one place I departed from a frozen term; commented at the key.

---

### Orchestration critique

**MEASURED**

1. **⭐ The eighth INVARIANT defect, and it is section 7.1's audit line.** `tail -n +8 "$F" | grep -nE ' as | as const|…'` **cannot return zero for a Romance-language catalog.** `as` is the Portuguese feminine plural definite article, and it occurs inside five string VALUES that are all correct and none of which may be touched: `"…tornam as contas…"`, `"…carregar as tuas partidas."`, `"Abrir as definições"`, `"Escolhe as peças a trocar"`, `"…carregar as partidas."`. The prompt then says "Expected result: ZERO hits. If you get one, it is a real weakening — fix it, do not scope it away", which instructs the Worker to damage the Portuguese. Catalog 1 could not find this: German has no bare word `as`. **This is not the same bug as the `tail -n +8` correction** — that fixed a collision with the *header*; this is a collision with *the target language*. I did not scope it away. I reworded my own English comments so the only surviving hits are genuine Portuguese articles, then proved the real property a different way: strip comments and string/template literals, and the token `as` appears **0 times in code**, along with 0 casts, 0 `Partial<`, 0 optional keys. Each other alternative in the audit independently returns 0. **Fix for the remaining six prompts:** replace ` as ` with a cast-shaped pattern such as `' as (const|unknown|any|never|string|number|Record|Partial|[A-Z][A-Za-z0-9_]*)\b'`, or make the audit strip string literals before grepping. **At least Afrikaans (`as` = as/than, axle) and Dutch (`as` = axle/ash) will hit this too**, so it is live for three of the six remaining catalogs, not just this one.
2. **Section 5.5's constrained-surface list is measured but partly mis-attributed, and it is in the wrong section.** The history table headings are named under "choose the shortest term", but they are the *least* constrained surface I checked: `min-w-full` table, `<th className="px-4 py-3">`, no nowrap, no minima. The ~5rem minima are ScorePanel's `min-w-[4.8rem] sm:min-w-[5.1rem]` score-name columns (`ScorePanel.tsx:382,395`). Everything else in the list verified exactly as written, including the `max-w-md` give-up-dialog correction and the `board.*` pill. Separately: **the whole list is language-independent and is labelled `[VARIANT: European Portuguese]`.** Six catalogs will now re-verify the same eight surfaces from six differently-worded copies. It belongs in an `[INVARIANT]` section, with only the *reason* it is high-risk staying variant.
3. **`header.logout` is the campaign's highest-value unlisted layout risk and no section names it.** 5.5 lists ScorePanel generically, but the specific collision — the standard pt-PT sign-out term is 15 characters against English's 6, on a nowrap `shrink-0` pill — is the kind of concrete pairing that 5.5 does name for `board.*`. Several remaining catalogs have the same problem (`Uitloggen`, `Afmelden`, `Logga ut`, `Skrá út`). Worth adding to the invariant list as a named key.
4. **Section 6 item 3 is incomplete about `game.aWord`.** It lists the no-helper functions, but `game.aWord` is a *text* key consumed as the `{word}` argument of `game.toast.aiPlayedWord` (`page.tsx:1003`), so its case and article have to compose inside another string. Trivial for Portuguese ("A AI jogou uma palavra"), but it is a composition constraint of exactly the class item 5 exists to catch, and it is unlisted.
5. **`history.unknownDate` serves two referents of different gender** — a date at `GameHistoryPanel.tsx:97` and a *username* at `ProfileModal.tsx:220`. Every gendered target language will hit this, and no section warns of it. It belongs beside section 6 item 5 as a third measured word-order/agreement trap.
6. **The prompt's own numbers all verified**: 296 + 20 = 316 keys; 467 passed / 3 skipped (I measured the baseline before mutating, so the comparison is real); eleven dynamic routes and zero static; the Next.js doc exists at the stated path; `pluralPt`'s signature and body match section 5.1 exactly; `portuguese.json` provenance is pt_PT as quoted. The "NINE WORDS" arithmetic in item 1 is right.

**LEAD**

1. Section 4 requires a comment "at any key whose CALL SITE constrained your word order", but `messages.de.ts` carries such a comment only at `board.zoomNoun`, not at `game.aiPlayedFor.before` where German reportedly abandoned the perfect tense. If that requirement is meant to hold across the campaign, catalog 1's file may be one comment short of it. **Unverified** — I read only the German file, not catalog 1's report, so I cannot tell whether the requirement post-dates that file. Flagging rather than asserting.
2. A one-line `[INVARIANT]` instruction to state, per language, which of the section 6 item 5 call sites turned out to be *harmless* would be cheap and useful. Portuguese needed no workaround at either site; German needed one at both. Three or four catalogs reporting "harmless" is evidence the call sites are fine as they are, which is information the eventual wiring slice would want.
3. Section 5.3's "pick ONE label style" is the right instruction, but every language will discover the same handful of keys that resist it — pagination pairs, toggle states, badge words. An `[INVARIANT]` sentence pre-authorising a small named exception list (rather than each catalog inventing its own justification) would make the eight files more comparable.
4. The commit body is asked to state the nine counted-noun forms while the nine *terminology* terms are explicitly banned from it. That asymmetry is deliberate and I followed it, but a reader of `git log` now gets half the vocabulary decisions and has to open the file for the other half. Consider moving the counted-noun forms into the file's comment block too, and having the commit body point at the file for both.
5. `Reasoning recommendation: High` was correct here, and the reason given (the plural rule plus the pt-PT boundary) is the right reason. The plural rule itself cost little once `plural.ts` was read; **the expensive part was gender and agreement**, which section 5.3 mentions in one clause. For Italian, German-adjacent and Nordic catalogs the same clause will carry most of the difficulty. It could be its own numbered item rather than a bullet.

---

**Report justification:** `new-mutation`
**Logical-whole closure:** not-closed
**Authority expiry:** my authority ended with this report. I did not begin a third catalog, add a locale, touch the wiring, or write anything into Meta; archiving this prompt/report pair is the ORCHESTRATOR's step.
**Context pressure:** low — roughly a third of the window used, no compaction.

**Smallest next step:** issue catalog 3 with section 7.1's ` as ` pattern replaced by a cast-shaped pattern (MEASURED #1), since Afrikaans and Dutch are both affected and the current line instructs a Worker to damage correct copy.
