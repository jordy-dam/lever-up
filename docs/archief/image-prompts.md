# Beeldprompts voor Lev

Doel: alle plaatjes uit `docs/brief.md` (sectie Beelden) met zo min mogelijk prompts, in Gemini of een andere beeldgenerator. Prompts zijn in het Engels omdat beeldmodellen dat beter volgen.

## Werkwijze: werk in sheets, niet per plaatje

Eén prompt, meerdere plaatjes op één vel, daarna knippen. Dat is sneller en Lev ziet er binnen een vel altijd hetzelfde uit.

| Stap | Wat | Prompts | Plaatjes |
|---|---|---|---|
| 1 | Karakterblad (referentie voor alles) | 1 (+ bijsturen) | 1 vel |
| 2 | Posesset | 1 vel van 8 | 8 |
| 3 | Oefeningen, start en eind naast elkaar | 1 vel per oefening (10) | 20 |
| 4 | Kaarten | 1 vel per soort (4), later per kaart | 24 |
| 5 | Badges en rangen | 2 vellen | ~10 |
| 6 | App-icoon | 1 | 1 |

Ongeveer 20 prompts in plaats van 60. Elke stap na stap 1 begint met het karakterblad als bijlage.

Regels:
- Chat in dezelfde conversatie blijven en het karakterblad als referentieplaatje meegeven. Verandert Lev toch: "Keep Lev exactly as in the reference sheet" toevoegen.
- Genereer eerst stap 1 en keur af totdat Lev goed is. Alles daarna erft dat.
- Transparante achtergrond lukt meestal niet echt. Vraag een effen lichtgrijze achtergrond (`#d9d9d9`) en haal die er daarna uit (Claude Code kan dat in bulk, zie onderaan).
- Controleer elk vel op: dezelfde pet met lime ringetje, geen extra vingers, ringen en parallettes kloppen, geen tekst in beeld.

## Stijlblok (plak dit in elke prompt)

```
STYLE LOCK: soft semi-realistic 3D-illustrated character, slightly stylised proportions,
clean smooth shading, light coming from the top left, calm muted colours.
Palette: dark navy, mid blue shirt, dark shorts, one lime-green accent only on the cap logo.
No text, no watermark, no speech bubbles. Generous empty margin around the subject.
```

## Stap 1: karakterblad

```
Character reference sheet of "Lev": an athletic man around thirty, short dark hair,
friendly confident expression, dark navy cap with a small lime-green ring as logo,
blue athletic t-shirt, dark shorts, sports shoes. Not based on any real person or existing character.
Layout: top row = full body front view, side view, back view, same height and scale.
Bottom row = six head-and-shoulders expressions: happy, focused, cheering, tired, surprised, proud.
Plain light-grey background (#d9d9d9). [STYLE LOCK]
```

## Stap 2: posesset (1 vel, 8 poses)

```
Using the attached character sheet, keep Lev exactly the same.
One sheet, 4 x 2 grid, each pose fully inside its own cell, plain light-grey background:
1 hanging from gymnastic rings, 2 front lever, 3 push-up on parallettes, 4 hollow body hold,
5 bodyweight squat, 6 cheering with both arms up, 7 tired and hunched, 8 thumbs up.
[STYLE LOCK]
```

## Stap 3: oefening in twee standen (sjabloon)

Eén vel per oefening, twee vakken naast elkaar, dezelfde camerahoek en kadrering, 4:3 per vak.

```
Using the attached character sheet, keep Lev exactly the same.
Two panels side by side, identical camera angle, framing and scale, 4:3 each.
Left panel: START position of "{OEFENING}". Right panel: END position of "{OEFENING}".
Show the equipment correctly ({MATERIAAL}). Plain light-grey background. [STYLE LOCK]
```

Eerst deze tien, in deze volgorde (voor scherm 1 en 3): Parallette push-ups, Ring rows, Pike push-ups, Hollow hold, Split squats, Tuck L-sit, Dead bug, Ring rows voeten verhoogd, Tuck hang, Front lever hold.

Later toevoegen met hetzelfde sjabloon (elk 1 vel): Diamond push-ups, Decline push-ups, Incline push-ups (zit al als kaart p1a), Leg raises, Stretches (per stretch een eigen vel). Bij elke nieuwe oefening hoort ook een regel in de spiergroepentabel in `docs/brief.md`.

## Stap 4: kaarten

Eerst 4 vellen met elk 6 staande kaartplaatjes (twee per niveau) voor duwen, trekken, core en benen. Staand formaat 3:4, Lev in beeld met de oefening van de kaart. Eigen plaatje per kaart pas later.

## Stap 5 en 6

Badges (trofee of medaille): Eerste sessie, Vijf keer raak, Consistentie-koning, Kaartenjager, Push-up held. Rangen: vijf emblemen (Kersverse hanger, Ringkind, Ringklimmer, Ringbaas, Ringleader). Icoon: de pet met lime ringetje op donkerblauw, 1024 x 1024. Prompts schrijf ik zodra stap 1 goed staat.

## Na het genereren

Plaatjes opslaan in `assets/` met de bestandsnamen uit de brief. Vellen knippen en achtergrond verwijderen doet Claude Code in bulk. Zet de ruwe vellen in `assets/_raw/`.
