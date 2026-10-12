# Gemini-prompts Lever-up

Eén document voor alle beelden. Alles werkt met **contactbladen**: zes beelden in een raster van 3 kolommen en 2 rijen op één plaatje, in dezelfde zaal en met dezelfde Lev. Jij maakt het blad, ik knip het in losse bestanden en plaats ze in de app. De oudere promptdocumenten staan in `docs/archief/`.

## Stand van zaken

| Beeldset | Waar in de app | Stand | Bestanden |
|---|---|---|---|
| Karakterblad van Lev | referentie voor alles | klaar | `assets/lev/character-sheet.webp` |
| Spierkaart (voor en achter) | uitgelicht oefeningscherm | klaar | `assets/muscles/` |
| Avatars (6) | header, profiel | klaar | `assets/avatars/a1..a6.webp` |
| Rangbeelden (Lev + 5 rangen) | Voortgang, Level up | klaar | `assets/ranks/` |
| **Lev-poses (6)** | rustscherm, afronden | **klaar (2026-10-11)** | `assets/lev/pose-*.webp` |
| **Oefeningen per soort (24, 4 bladen)** | kaarten, focusscherm, uitgelicht scherm | **volgende** | `assets/cards/<id>.webp` |
| Begin- en eindposities (8 oefeningen) | wisselend plaatje op het uitgelichte scherm | later | `assets/exercises/` |
| Badges (4) en app-icoon | Voortgang, telefoon | later | `assets/badges/`, `assets/icons/` |

## Zo werk je

1. Geef bij **elke** prompt het karakterblad van Lev mee (`assets/lev/character-sheet.webp`).
2. Plak het **stijlblok** hieronder, en daarna de prompt van het blad.
3. Heb je al een goedgekeurd blad (bijvoorbeeld de rangbeelden)? Voeg dat ook toe als tweede referentie: "zelfde zaal, zelfde camera, zelfde stijl".
4. Sla het blad op als PNG in `assets/_raw/` en geef het aan mij, of knip het zelf met het commando onderaan.
5. Niet goed? Zeg wat er mis is in plaats van "maak opnieuw". Een afwijkende zaal of een andere Lev is wel een reden om opnieuw te beginnen.

## Stijlblok (plak dit vóór elke prompt)

```
Gebruik de bijgevoegde karakterreferentie voor Lev: een atletische man van rond de dertig, korte donkere haren, donkerblauwe pet met een lime-groen ringetje als logo, helderblauw sportshirt, donkere short, grijze sokken, donkere sportschoenen. Vriendelijke, zelfverzekerde uitdrukking. Teken hem exact zo, met hetzelfde gezicht, dezelfde proporties en dezelfde kleding.

Stijl: platte 2D-cartoon, schone dikke contouren, vlakke kleurvlakken met eenvoudige schaduwvlakken, geen gradients, geen fotorealisme, geen 3D-glans. Lichtinval altijd van linksboven, zachte schaduw op de vloer rechts van Lev. Geen tekst, geen logo's, geen watermerk, geen extra personen.

Achtergrond (in elk beeld identiek): volledig effen donkerblauw (#101c38), geen wand, geen paneelband, geen rek, geen schijven, geen ramen, geen verloop. Alleen een egale vloer in iets lichter leisteenblauw (#1a2540) met een zachte schaduw onder Lev en de uitrusting, vloerlijn op 82% van de hoogte. Niets anders in beeld dan Lev en de uitrusting van de oefening. Kleurpalet beperkt tot marineblauw, leisteen, Lev's blauw, huidtinten en staal-grijs voor de uitrusting; lime alleen als ringetje op de pet.

Camera (vast): zijaanzicht op borsthoogte, horizontaal, geen perspectiefvertekening. Lev en zijn uitrusting staan als één geheel in het midden, volledig in beeld, met ruime marge rondom. De hele uitrusting past in het beeld, ook de stang of de palen helemaal tot boven en onder. Lev is ongeveer 60% van de beeldhoogte; de uitrusting mag hoger zijn.

Uitvoering: toon de oefening technisch exact zoals beschreven, in het midden van de beweging, zonder extra bewegingen of hulpmiddelen. Bij twijfel: de beschrijving volgt letterlijk, geen eigen interpretatie.
```

## Volgende 1: Lev-poses (1 blad)

Waar: het rustscherm toont `pose-tired` in de ring (de andere kunnen daar later wisselen), de rest is voor het afrondpaneel en tips. Tot die tijd gebruikt de app Lev's gezicht.

```
Maak één afbeelding met zes beelden in een raster van 3 kolommen en 2 rijen (3:2 liggend, bijvoorbeeld 3072 x 2048). Elk beeld staat in een eigen vierkant van exact dezelfde grootte, zonder kaders, tekst of nummers, in de vaste zaal uit de stijlinstructie, Lev volledig in beeld en in het midden. Vriendelijk en een beetje grappig.

Bovenste rij, van links naar rechts:
1. Moe maar tevreden: Lev staat voorovergebogen met zijn handen op zijn knieën, een zweetdruppel, een grijns.
2. Water drinken: Lev drinkt uit een bidon, hij leunt ontspannen met een elleboog op het klimrek.
3. Rekken: Lev rekt zijn armen boven zijn hoofd uit en zijn ogen zijn dicht, een lange ademhaling.
Onderste rij, van links naar rechts:
4. Juichen: Lev springt met beide armen omhoog en een brede lach.
5. Duim omhoog: Lev kijkt de kijker aan en steekt zijn duim op.
6. Idee: Lev wijst met een vinger omhoog, boven zijn hoofd een kleine lamp, zijn andere hand op zijn heup.
```

## Volgende 2: Oefeningen per soort (4 bladen, 24 beelden)

Eén sleutelbeeld per oefening, in het midden van de beweging. Het dient voor de kaart, het focusscherm en het uitgelichte scherm; de app pakt `assets/cards/<id>.webp` voor alle drie. Gebruik het stijlblok plus het blad voor één soort. Alle vier delen deze opbouw (herhaal die dus in elk blad):

```
Maak één afbeelding met zes beelden in een raster van 3 kolommen en 2 rijen (3:2 liggend, bijvoorbeeld 3072 x 2048). Elk beeld staat in een eigen vierkant van exact dezelfde grootte, zonder kaders, tekst of nummers, in de vaste zaal uit de stijlinstructie, Lev volledig in beeld en in het midden, met de uitrusting van de oefening erbij. Je ziet duidelijk hoe de oefening wordt gedaan.
```

**Blad Duwen** (`cards-duwen.png`, volgorde p1a p1b p2a p2b p3a p3b)
```
Bovenste rij: 1. Incline push-ups: handen op een stevige bank, schuine plank. 2. Langzame wall push-ups: schuin tegen de muur, handen op de muur, borst dichtbij. 3. Push-ups: klassieke push-up op de vloer, plank bovenaan.
Onderste rij: 4. Pike push-ups: omgekeerde V op de vloer, hoofd tussen de armen. 5. Parallette push-ups: twee lage parallettes, borst laag ertussen. 6. Ring push-ups: handen op lage ringen, push-up.
```

**Uitvoeringsregels (herhaal in elk blad)**: de prompts hieronder beschrijven elke oefening met vier vaste punten: houding van het lichaam, plek en vorm van de uitrusting, handgreep en richting. Gemini verwisselt anders hangen en duwen en chin-up en pull-up. Voeg dit toe onder de beschrijvingen:

```
Let op: dit zijn trek- en hangbewegingen waar dat staat. Bij elke hangoefening hangt Lev ONDER de stang of ringen met zijn armen boven zijn hoofd, zijn voeten van de grond (behalve bij ring rows). Hij staat of ligt NIET op de grond te duwen. De stang is een horizontale stalen stang tussen twee verticale palen; de palen zijn minstens 40 cm langer dan Lev lang is en staan volledig in beeld, de stang zit boven Lev's hoofd. Handgreep: pull-up = handpalmen van Lev af (overhand, schouderbreed of iets breder); chin-up = handpalmen naar Lev toe (onderhand, schouderbreed); ringen = neutraal, handpalmen naar elkaar. Controleer: palen hoger dan de persoon, juiste greep, juiste houding.
```

**Blad Trekken** (`cards-trekken.png`, volgorde t1a t1b t2a t2b t3a t3b)
```
Bovenste rij: 1. Ring rows, hoge hoek: bijna rechtop hangend aan ringen, borst naar de ringen. 2. Scapula-hang: Lev hangt onder een rekstok met gestrekte armen boven zijn hoofd, voeten van de grond, overhandse greep (handpalmen van hem af), schouders omlaag getrokken. 3. Ring rows, lage hoek: bijna horizontaal onder de ringen.
Onderste rij: 4. Chin-up negatives: Lev hangt onder de stang met onderhandse greep (handpalmen naar hem toe), armen half gebogen, kin net boven de stang, langzaam zakkend. 5. Pull-ups: Lev hangt onder de stang met overhandse greep (handpalmen van hem af), kin boven de stang, voeten van de grond. 6. Ring rows, voeten verhoogd: horizontaal onder de ringen, voeten op een lage houten kist.
```

**Blad Core** (`cards-core.png`, volgorde c1a c1b c2a c2b c3a c3b)
```
Bovenste rij: 1. Dead bug: liggend op een dunne mat, tegengestelde arm en been gestrekt. 2. Plank: onderarmplank, rechte lijn. 3. Hollow hold: liggend op een mat, schouders en benen los van de grond, onderrug plat.
Onderste rij: 4. Hanging knee raises: hangend aan een stang, knieën naar de borst. 5. Tuck L-sit op parallettes: opgetrokken knieën in steun op twee parallettes. 6. Hollow rocks: gewiegd in een stijve hollow positie op een mat.
```

**Blad Benen** (`cards-benen.png`, volgorde l1a l1b l2a l2b l3a l3b)
```
Bovenste rij: 1. Squats: diepe squat, armen naar voren. 2. Glute bridges: liggend op een mat, heupen omhoog, schouders op de mat. 3. Split squats: diepe split squat, rechtop.
Onderste rij: 4. Wall sit: rug plat tegen de muur, bovenbenen horizontaal. 5. Pistol squat naar bank: zakkend op één been naar een bank, het andere been gestrekt voor. 6. Jump squats: in de lucht, benen gestrekt, armen omhoog.
```

## Losse prompts: de vier hangoefeningen

Eén plaatje per prompt, vierkant (1:1, bijvoorbeeld 2048 x 2048). Geef het karakterblad mee, plak het stijlblok en daarna de prompt. De regels staan in elke prompt zelf, zodat ze niet verloren gaan.

Gedeeld voor alle vier (zit al in de prompts, hier ter controle): Lev hangt ONDER de stang, armen boven zijn hoofd; twee verticale stalen palen, minstens 40 cm hoger dan Lev, volledig in beeld van vloer tot boven; de stang horizontaal tussen de palen boven Lev; effen achtergrond.

**Scapula-hang** (`t1b`)
```
Eén afbeelding, vierkant, van Lev in een scapula-hang. Zijaanzicht. Een horizontale stalen stang tussen twee verticale stalen palen; de palen staan helemaal in beeld, van de vloer tot boven de stang, en zijn duidelijk hoger dan Lev, de stang zit boven zijn hoofd. Lev hangt ONDER de stang, zijn voeten hangen vrij boven de vloer. Zijn armen zijn volledig gestrekt omhoog, overhandse greep: zijn handpalmen wijzen van hem af, handen iets breder dan zijn schouders. Zijn schouders zijn actief omlaag getrokken (hij hangt "gespannen", niet slap), borst iets naar voren. Hij kijkt rustig voor zich uit. Hij staat niet op de grond en hij duwt niet.
```

**Chin-up negatives** (`t2b`)
```
Eén afbeelding, vierkant, van Lev in de langzame zakkende fase van een chin-up. Zijaanzicht. Een horizontale stalen stang tussen twee verticale stalen palen; de palen staan helemaal in beeld, van de vloer tot boven de stang, en zijn duidelijk hoger dan Lev, de stang zit boven zijn hoofd. Lev hangt ONDER de stang, voeten vrij boven de vloer, kin net boven de stang, armen ongeveer halfgebogen. Onderhandse greep: zijn handpalmen wijzen NAAR HEM TOE, handen op schouderbreedte, duimen om de stang. Zijn gezicht toont inspanning en controle. Hij staat niet op de grond en hij duwt niet.
```

**Pull-ups** (`t3a`)
```
Eén afbeelding, vierkant, van Lev bovenaan een strakke pull-up. Zijaanzicht. Een horizontale stalen stang tussen twee verticale stalen palen; de palen staan helemaal in beeld, van de vloer tot boven de stang, en zijn duidelijk hoger dan Lev, de stang zit boven zijn hoofd. Lev hangt ONDER de stang, voeten vrij boven de vloer, zijn kin boven de stang, borst naar de stang, ellebogen naar beneden en naar achter. Overhandse greep: zijn handpalmen wijzen VAN HEM AF, handen iets breder dan schouderbreed. Zijn lichaam is recht en gespannen. Hij staat niet op de grond en hij duwt niet.
```

**Hanging knee raises** (`c2b`)
```
Eén afbeelding, vierkant, van Lev bovenaan een hanging knee raise. Zijaanzicht. Een horizontale stalen stang tussen twee verticale stalen palen; de palen staan helemaal in beeld, van de vloer tot boven de stang, en zijn duidelijk hoger dan Lev, de stang zit boven zijn hoofd. Lev hangt ONDER de stang met gestrekte armen, overhandse greep (handpalmen van hem af), handen op schouderbreedte, voeten vrij boven de vloer. Zijn knieën zijn opgetrokken tot voor zijn borst, bovenbenen ongeveer horizontaal of hoger, onderbenen hangend, zijn bekken licht gekanteld. Hij staat niet op de grond en hij duwt niet.
```

Controle per resultaat: zijn de palen hoger dan Lev en volledig in beeld, hangt hij onder de stang, klopt de greep? Zo niet, zeg welk van de drie fout is.

Knippen (één vierkant plaatje per bestand):

```
python3 tools/sheet-cut.py assets/_raw/hang-t1b.png assets/cards t1b --cols 1
python3 tools/sheet-cut.py assets/_raw/hang-t2b.png assets/cards t2b --cols 1
python3 tools/sheet-cut.py assets/_raw/hang-t3a.png assets/cards t3a --cols 1
python3 tools/sheet-cut.py assets/_raw/hang-c2b.png assets/cards c2b --cols 1
```

## Later: begin- en eindposities (animatie)

Voor een wisselend plaatje op het uitgelichte scherm (nu staat er één beeld). Per oefening een start- en een eindbeeld in dezelfde zaal, 4:3, het eindbeeld als bewerking van het startbeeld: "Behoud alles exact hetzelfde. Verander alleen de houding van Lev naar: ...". Bestanden: `assets/exercises/<naam-met-streepjes>-start.webp` en `-end.webp`. Het Parallette-paar dat er nu staat heeft een lichte achtergrond en past er niet bij; vervang het.

| Oefening | Start | Eind |
|---|---|---|
| Parallette push-ups | plank bovenaan op de parallettes | borst laag tussen de parallettes |
| Ring rows | achterover onder de ringen, armen gestrekt | borst bij de ringen |
| Pike push-ups | omgekeerde V, heupen hoog | hoofd laag richting de vloer |
| Hollow hold | liggend op de rug, armen boven het hoofd | schouders en benen los van de grond |
| Ring rows, voeten verhoogd | horizontaal, voeten op de kist | borst bij de ringen |
| Split squats | rechtop in spreidstand | diep, achterste knie bijna op de grond |
| Tuck L-sit op parallettes | steun op gestrekte armen, voeten op de vloer | knieën opgetrokken, voeten los |
| Dead bug | armen omhoog, knieën 90 graden | tegengestelde arm en been gestrekt |

## Later: badges en app-icoon

- **Badges (blad 2 x 2, `badges-sheet.png`)**: vierkant, platte vormen, lime accent op marineblauw, geen tekst. Volgorde: `eerste-sessie` (ster), `vijf-keer-raak` (een vijf), `consistentie-koning` (kroon boven een kalender), `kaartenjager` (waaier van kaarten). De app tekent nu zelf medailles; de beelden komen later.
- **App-icoon (1 beeld)**: `assets/icons/source-1024.png`, 1024 x 1024, Lev's hoofd met pet in een cirkel op marineblauw met een lime ring, 10% marge rondom. Het icoon in de app is nu een tijdelijk avatarbeeld.

## Klaar (alleen voor opnieuw maken)

**Avatars** (`avatars-sheet.png`, 3 x 2, alleen hoofd en schouders op effen marineblauw #1b2a4d, iedereen met de Lever-up pet en een blauw shirt, niet Lev): 1 man licht, korte bruine haren; 2 man donker, kort krullend zwart haar; 3 man Oost-Aziatisch, kort zwart haar; 4 vrouw licht, bruine staart onder de pet; 5 vrouw donker, lang krullend haar of vlechten onder de pet; 6 vrouw Oost-Aziatisch, lang zwart haar in een staart onder de pet.

**Rangbeelden** (`ranks-sheet.png`, 3 x 2, de vaste zaal, steeds moeilijker): 1 algemeen, Lev zwaait; 2 Groentje, wiebelige push-up op de knieën met een zweetdruppel; 3 Veertje, pull-up aan de stang met één oog dicht en trillende sterretjes; 4 Bar Baas, trots bovenop de stang met duim omhoog; 5 Lucht Ninja, horizontaal aan een paal als een vlag met windstrepen; 6 Legende, zwevend in kleermakerszit met een zachte lichte rand.

## Knippen

Elk blad wordt een rij vierkante webp-bestanden van 512 px. Vereist pillow (`pip install pillow`).

```
python3 tools/sheet-cut.py assets/_raw/poses-sheet.png assets/lev pose-tired pose-water pose-stretch pose-cheer pose-thumbs-up pose-idea
python3 tools/sheet-cut.py assets/_raw/cards-duwen.png assets/cards p1a p1b p2a p2b p3a p3b
python3 tools/sheet-cut.py assets/_raw/cards-trekken.png assets/cards t1a t1b t2a t2b t3a t3b
python3 tools/sheet-cut.py assets/_raw/cards-core.png assets/cards c1a c1b c2a c2b c3a c3b
python3 tools/sheet-cut.py assets/_raw/cards-benen.png assets/cards l1a l1b l2a l2b l3a l3b
python3 tools/sheet-cut.py assets/_raw/badges-sheet.png assets/badges eerste-sessie vijf-keer-raak consistentie-koning kaartenjager --cols 2
```

De app pakt alles vanzelf op zodra een bestand er staat; tot die tijd toont hij een plaatshouder of een getekende terugval.
