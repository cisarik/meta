# ContextDeck — the keyboard is the interface

Handoff for a fresh Orchestrator. Paste this whole file as the first message.
Talk to the COOPERATOR in Slovak. Write repository files and Worker prompts in
English. He carries every prompt and report by hand. Do not dispatch subagents.

He is not a designer. He reviews by running the app and sending a screenshot,
or by answering `PASS`. Implement a presentation slice, rebuild, and tell him
what to look at. He Quits the old process and starts `./build/contextdeck`.
You do not launch it. You do not commit or push unless he asks. Screenshots
belong in his META archive, never in the product repository.

## The idea

ContextDeck should feel like looking at the keyboard, not like reading a
settings file. The only picture in the product is the G213, drawn as five
zones. Everything else is quiet type on the Breeze theme. The green selection
in the drawer is the only chrome accent. Saturated color appears only inside
the five zones, and only when those colors are the user's desired colors.

He should recognize his keyboard before he reads a sentence.

That is the whole visual program. Do not add a second theme, a custom font, a
marketing illustration, a gradient behind the window, or per-key art. The G213
does not have per-key RGB. Drawing keycaps would be a lie.

## What is already done, so you do not redo it

Local `main` commit `029e2185c4f28976bc24ed06bdc8f263ec6b2a0f`
(`ui: say what the settings screen is doing`) is the parent. Public
`origin/main` may still be `4cadc669ea759aa367871a58639b19398273a87f` until he
pushes. Verify. Do not reset.

On top of that commit, the working tree already contains an uncommitted
cleanup. Read the diff before editing. It is presentation only:

- The tray menu is Slovak: the status sentence, Sledovať profil, Zhasnúť,
  Predvolené firmware, Nastavenia…, Ukončiť. Sleep, display-off, and keyboard
  claim are gone from the tray. Left click still opens Settings.
- Diagnostika names consequences. Prevziať klávesnicu, zhasnutie obrazoviek,
  and uspatie each ask first. Vrátiť bežné písanie and Vzdať sa držania
  klávesnice run immediately so the keyboard can be freed in one step. The
  words LEASE and ARM survive only inside Zobraziť technické podrobnosti.
  The pause note no longer says compositor or D-Bus.
- Aplikácie hides the empty inventory combo and the add button while the KWin
  bridge is disconnected, and keeps the orange explanation.
- Plochy shows the session editor, the preview, and Použiť only after
  Povoliť správu plôch is on. The word `rows` is gone from the preview.
- Čierna means vypnuté. Direct is called vlastné farby. The temporary-color
  banner no longer pastes an English diagnostic token into a Slovak sentence.
- Pokročilé no longer prints the host keyboard layout.

Do not spend the first session re-translating this. He deleted the previous
handoff because it was a chore list. This one is the design.

`lightingLabel()` still returns the English diagnostic phrases
(`untouched — device default`, `temporary override`, `off`). Leave those
tokens. `docs/testing.md` still expects them. The screen already speaks Slovak
through other strings.

## Invariants you must not break while making it beautiful

- One keyboard, five zones, order left, middle, right, arrows-and-home, numpad.
  Internal names in `kZoneNames` stay English. The screen says Ľavá, Stred,
  Pravá, Šípky, Numerická.
- The session app never grabs the device. The broker stays inactive. Do not
  ARM, do not suspend, do not blank the displays, do not press Použiť during
  a review. He may open a dialog and must cancel it.
- Workspace changes happen only on Použiť. Nothing launches at login.
- OpenRGB being down is a normal state. The UI must look finished while
  lighting is disabled. Do not start OpenRGB to make the screenshot prettier.
- Wave, Cycle, and Breathing may remain the names of firmware effects.
- No new dependency. No license edit. M2, M3, M4, and the gates G3, G4, G6,
  G7, G8 stay deferred. Whole `ui-ux-refinement` is not closed.
- `Kirigami.InlineMessage` is invisible unless `visible` is set.

## The picture of the keyboard

Replace the five equal rectangles in `ui/ZoneHero.qml`.

The shape is one horizontal instrument:

- Three zones share the alphanumeric mass. Left is slightly narrower than the
  middle, the middle is the widest, the right matches the left. They touch,
  with only a hairline gap.
- A clear gap, then a shorter arrow cluster.
- A second gap, then the numpad, taller than the arrow cluster and detached,
  like the real board.

Untouched firmware stays a calm dashed outline at rest. No pulsing. No fake
Wave animation. When the mode is direct, the five regions fill with the
desired colors. When the mode is off, they are black, and the badge says
Vypnuté. The badge sits on the numpad corner, short: `Predvolené (Wave)` or
the effect name.

This hero is used in two sizes. Stav shows it large, almost alone, with the
three facts Svetlo, Kontext, Spojenie underneath and nothing else competing
except Nastaviť farby. Farby shows the same hero and edits it.

## Farby is a bench, not a scroll

The window is already about 1040 pixels wide and the drawer is open. Use that
width. On Farby, put the keyboard on the left and the controls on the right:
preset, the controls that belong to that preset, then Uložiť. Speed and
breathing stay hidden unless the mode is wave, cycle, or breathing. Hex stays
behind its switch. The gradient is a second group, not the first thing under
the combo.

The sentence about what the zones mean sits with the two layout buttons,
beside the keyboard, not under a long editor. A person reads the consequence
before Použiť rozloženie 4 plochy + aplikácia.

Uložiť is the primary button and it is visually quiet until something in the
editor is dirty. `LightingPresetEditor` already has `readyToSave`. Use that.
Do not invent a second save path. There is no global dirty bit for the whole
document yet. Do not build one in the first visual slice.

## Stav is a glance

After the hero exists, Stav should be the glance and Farby the bench. Stav
does not grow new sections. If a fact does not fit in Svetlo, Kontext, or
Spojenie, it does not belong on Stav.

The three facts stay a label column of stable width and a bold value. Do not
turn them into colored pills.

## Plochy is a map of desks he can see

He has three desktops and the page already knows the count, the current
ordinal, the grid, and wrapping. When management is off, that observation is
the whole page, plus the two checkboxes. That part is in the working tree.
Keep it.

When management is on, do not return to a specification form as the first
view. Draw the observed desktops as a row of cells, current one marked, and
put the dry-run result in those cells: no change, create, or rename. Použiť
sits under that row. The long explanation of checkpoint behavior belongs in
the remove-extras dialog, which already exists, not under the buttons.

Never press Použiť to try the drawing. A disabled button and a preview are
enough evidence.

## Aplikácie is one profile at a time

Today a profile repeats the entire lighting editor. That will become a stack
of keyboards. The shape to aim at: a list of profile names, one selected, and
the bench from Farby bound to that profile. Empty and disconnected stay the
states already written. Do not add a retry button. There is no reload call.

The removal dialog copy stays as it is.

## Danger is a breaker panel

Diagnostika's wording is done. The next visual step is separation, not more
synonyms. Sleep, display-off, and taking the keyboard are three large rows,
each with one consequence sentence and one button. They are not a wrap of
five tool buttons. Recovery (return typing, give up the hold) is a second,
quieter pair, because those must stay one click.

Do not put any of them back on the tray.

## Motion and material

One motion is allowed: a zone color may ease to its new color in about 150
milliseconds when the desired color changes. Idle state does not move.
Dashed outlines do not breathe. Pages do not fade in.

Material is Kirigami. Cards only where a group is a real object (the keyboard,
the desktop row, one profile). Do not card every label.

## How to proceed with him

1. Verify the checkout. If his worktree still has the uncommitted cleanup,
   keep it. It is the baseline. If he has committed it, that commit is the
   baseline. Do not redo the cleanup either way.
2. Build the hero first, on Stav only. Show him that screenshot before
   touching Farby. This is the slice that decides whether the picture is right.
3. Then move that same hero into Farby and split the page into bench and
   controls.
4. Then the desktop row on Plochy.
5. Then one-profile-at-a-time on Aplikácie.
6. Then the breaker panel on Diagnostika.

Stop after each. If he says the picture is wrong, fix the picture before
adding the next page. Do not open a parallel cleanup campaign.

Rebuild with `cmake --build build`. A linked `contextdeck` typechecks the QML.
Run the 21 CTest names before any commit he requests if you changed C++.
For a QML-only hero, the link is the gate and his screenshot is the acceptance
of the look.

## What you must not claim

A beautiful hero is not a five-zone hardware test. OpenRGB refused, the portal
app-id warning, and a disconnected KWin bridge are not UI failures. The whole
`ui-ux-refinement` is not closed. Do not start the broker to finish the design.
