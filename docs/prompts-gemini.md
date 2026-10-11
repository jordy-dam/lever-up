# Gemini-prompts Lever-up

Alles wat je nodig hebt om de beelden te maken. Werk in deze volgorde zodat Lev en de ruimte overal gelijk blijven.

## Zo werk je

1. **Referentie bijvoegen bij elke prompt:** `assets/lev/character-sheet.webp` (het goedgekeurde karakterblad).
2. **Stijlblok plakken** (hieronder) en daarachter de scène-regel van het plaatje.
3. **Eerste goedgekeurde oefeningplaatje bijvoegen als tweede referentie** bij alle volgende plaatjes ("zelfde ruimte, zelfde camera, zelfde stijl").
4. **Eindpositie maken als bewerking van de startpositie:** voeg het startplaatje toe en zeg: "Behoud alles exact hetzelfde (ruimte, camera, licht, kleding, uitrusting). Verander alleen de houding van Lev naar: ..."
5. Sla op als PNG (of WebP) met de bestandsnaam uit de tabel. Ik zet ze om en plaats ze in de app.
6. Niet goed? Zeg erbij wat er mis is, niet "maak opnieuw". Een afwijkende kamer is een reden om opnieuw te beginnen.

## Stijlblok (plak dit boven elke prompt)

```
Gebruik de bijgevoegde karakterreferentie voor Lev: een atletische man van rond de dertig, korte donkere haren, donkerblauwe pet met een lime-groen ringetje als logo, helderblauw sportshirt, donkere short, grijze sokken, donkere sportschoenen. Vriendelijke, zelfverzekerde uitdrukking. Teken hem exact zo, met hetzelfde gezicht, dezelfde proporties en dezelfde kleding.

Stijl: platte 2D-cartoon, schone dikke contouren, vlakke kleurvlakken met eenvoudige schaduwvlakken, geen gradients, geen fotorealisme, geen 3D-glans. Lichtinval altijd van linksboven, zachte schaduw op de vloer rechts van Lev. Geen tekst, geen logo's, geen watermerk, geen extra personen.

Vaste ruimte (in elk plaatje identiek): een donkere sportschool, vlak getekend. Achterwand effen donkerblauw (#101c38) met één iets lichtere horizontale paneelband op 45% van de hoogte. Vloer donker leisteenblauw (#1a2540) met één dunne lichtere lijn op de wandrand. Links aan de rand een stukje klimrek (wall bars) in staal, rechts aan de rand een rek met gewichtsschijven, beide gedempt en nauwelijks afleidend, altijd op dezelfde plek. Geen ramen, geen publiek. Kleurpalet beperkt tot marineblauw, leisteen, Lev's blauw en huidtinten; lime alleen als ringetje op de pet.

Camera (vast): zijaanzicht op borsthoogte, horizontaal, geen perspectiefvertekening. Lev staat of ligt in het midden van het beeld, volledig in beeld, ongeveer 70% van de beeldhoogte, ruime marge rondom. De vloerlijn ligt op 82% van de hoogte, handen en voeten raken die lijn. De uitrusting voor de oefening staat in het midden bij Lev.
```

## 1. Oefeningplaatjes (4:3, 2 per oefening)

Formaat 4:3 (bijvoorbeeld 2048 x 1536). Elke oefening: eerst start, daarna eind als bewerking van start.

| Bestand | Uitrusting | Start | Eind |
|---|---|---|---|
| `parallette-push-ups-start` / `-end` | twee lage parallettes naast elkaar in het midden | Plank bovenaan: armen gestrekt op de parallettes, lichaam in een rechte lijn, voeten op de vloer | Borst laag tussen de parallettes, ellebogen ongeveer 90 graden, lichaam nog steeds recht |
| `ring-rows-start` / `-end` | ringen aan een stalen rek, ophanghoogte op heuphoogte | Lev hangt achterover onder de ringen, armen gestrekt, lichaam recht, hielen op de vloer | Borst bij de ringen, ellebogen naar achter, lichaam recht |
| `pike-push-ups-start` / `-end` | geen, alleen vloer | Omgekeerde V: heupen hoog, armen en benen gestrekt, hoofd tussen de armen | Hoofd laag richting de vloer, ellebogen gebogen, heupen nog hoog |
| `hollow-hold-start` / `-end` | een dunne gymmat op de vloer | Liggend op de rug, armen boven het hoofd, benen gestrekt, ontspannen | Hollow hold: schouders en gestrekte benen van de grond, onderrug plat, armen naast de oren |
| `ring-rows-voeten-verhoogd-start` / `-end` | ringen aan een rek op heuphoogte, voeten op een lage houten kist | Lichaam recht en horizontaal, armen gestrekt, voeten op de kist | Borst bij de ringen, ellebogen naar achter, lichaam horizontaal |
| `split-squats-start` / `-end` | geen | Staand in spreidstand, een been voor, achterste knie boven de grond, rechtop | Diep: voorste bovenbeen horizontaal, achterste knie bijna op de grond, romp rechtop |
| `tuck-l-sit-op-parallettes-start` / `-end` | twee lage parallettes in het midden | Steun op gestrekte armen op de parallettes, voeten nog op de vloer | Voeten van de grond, knieën opgetrokken tegen de borst, armen gestrekt |
| `dead-bug-start` / `-end` | een dunne gymmat | Liggend op de rug, armen recht omhoog, knieën 90 graden boven de heupen | Rechterarm boven het hoofd en linkerbeen gestrekt vlak boven de grond, de rest blijft gelijk |

Extra (voor later): `front-lever-hold-start` (opgetrokken en gehurkt hangend aan de ringen) en `-end` (horizontale front lever).

## 2. Kaartplaatjes (24, vierkant 1:1)

Formaat 1:1 (bijvoorbeeld 1536 x 1536). Zelfde ruimte en camera, één houding in het midden van de beweging, Lev groot en leesbaar. Bestand: `assets/cards/<id>.webp`.

| ID | Oefening | Scène |
|---|---|---|
| p1a | Incline push-ups | handen op een stevige bank, schuine plank |
| p1b | Langzame wall push-ups | staand schuin tegen de muur, handen op de muur, borst dichtbij |
| p2a | Push-ups | klassieke push-up op de vloer, plank bovenaan |
| p2b | Pike push-ups | omgekeerde V op de vloer |
| p3a | Parallette push-ups | borst laag tussen twee parallettes |
| p3b | Ring push-ups | push-up met handen op lage ringen |
| t1a | Ring rows, hoge hoek | bijna rechtop hangend aan ringen, borst naar de ringen |
| t1b | Scapula-hang | hangend aan een rekstok, armen gestrekt, schouders omlaag getrokken |
| t2a | Ring rows, lage hoek | bijna horizontaal onder de ringen |
| t2b | Chin-up negatives | boven de stang, langzaam zakkend, kin boven de stang |
| t3a | Pull-ups | strakke pull-up, kin boven de stang |
| t3b | Ring rows, voeten verhoogd | horizontaal onder de ringen, voeten op een kist |
| c1a | Dead bug | liggend, tegengestelde arm en been gestrekt |
| c1b | Plank | onderarmplank, rechte lijn |
| c2a | Hollow hold | hollow hold liggend op een mat |
| c2b | Hanging knee raises | hangend aan een stang, knieën naar de borst |
| c3a | Tuck L-sit op parallettes | opgetrokken knieën in steun op parallettes |
| c3b | Hollow rocks | gewiegd in hollow positie op een mat |
| l1a | Squats | diepe squat, armen naar voren |
| l1b | Glute bridges | liggend, heupen omhoog, schouders op de mat |
| l2a | Split squats | diepe split squat |
| l2b | Wall sit | rug tegen de muur, bovenbenen horizontaal |
| l3a | Pistol squat naar bank | op een been zakkend naar een bank, andere been gestrekt voor |
| l3b | Jump squats | in de lucht, benen gestrekt, armen omhoog |

Optioneel kader per soort, voor later: duwen, trekken, core, benen.

## 3. Lev-poses (8, 4:3, effen lichtgrijze achtergrond)

Voor Level up, lege staten en de afrondschermen. Bestand: `assets/lev/pose-<naam>.png`. Gebruik hier een effen lichtgrijze achtergrond zodat ik hem vrij kan maken; Lev vult 80% van de hoogte.

`pose-tired` wordt gebruikt op het rustscherm van de geleide sessie (Lev ademt rustig, ring eromheen). `pose-hang` (hangend aan de ringen), `pose-front-lever`, `pose-pushup`, `pose-hollow`, `pose-squat`, `pose-cheer` (juichend, armen omhoog), `pose-tired` (moe, handen op de knieën), `pose-thumbs-up`.

## 4. Gezichten voor avatar en Level up (2)

Hoofd en schouders, vierkant, effen lichtgrijze achtergrond: `assets/lev/avatar.webp` (blij) en `assets/lev/face-cheer.webp` (trots). Nu uitgesneden uit het karakterblad; vervangen door echte plaatjes verbetert de scherpte.

## 5. Badges, rangen en icoon

Allemaal vierkant, flat, vlakke vormen, lime accent, marineblauwe ondergrond, geen tekst.

- **Rangemblemen (5):** `assets/ranks/groentje`, `veertje`, `bar-baas`, `lucht-ninja`, `legende`. Een ronde badge op marineblauw met lime rand, in dezelfde platte stijl als Lev. Elk embleem toont Lev als cartoon-poppetje, steeds verder losgekomen van de zwaartekracht, zonder tekst en zonder felle gloed:
  1. **groentje:** zweetdruppelend poppetje dat probeert op te drukken.
  2. **veertje:** poppetje met een oog dicht dat een pull-up probeert, kleine trillende sterretjes eromheen.
  3. **bar-baas:** Lev steekt trots een duim op naar een poppetje bovenop een stang.
  4. **lucht-ninja:** poppetje horizontaal in de lucht, zachte windstrepen langs de ledematen.
  5. **legende:** poppetje dat zweeft met een zachte lichte rand (geen felle gloed), Lev valt verbaasd flauw op de achtergrond.
- **Badges (4 nu):** `assets/badges/eerste-sessie` (ster), `vijf-keer-raak` (vijf), `consistentie-koning` (kroon boven een kalender), `kaartenjager` (waaier van kaarten). Later: `push-up-held`.
- **App-icoon (1):** `assets/icons/source-1024.png`, 1024 x 1024: Lev's hoofd met pet in een cirkel op marineblauw met een lime ring. Marge van 10% rondom.

## 6. Avatars voor de gebruiker (6, vierkant 1:1)

De gebruiker kiest er één in Profiel. Lev blijft de trainer; dit zijn de sporters. Zelfde stijlblok en dezelfde ruimte-kleuren als hierboven, maar alleen hoofd en schouders op een effen marineblauwe achtergrond (#1b2a4d), midden in beeld, ruime marge, vriendelijke zelfverzekerde uitdrukking. Iedereen draagt de donkerblauwe Lever-up pet met het lime-groene ringetje en een blauw sportshirt (dezelfde als Lev), zodat ze bij hem passen. Geef Gemini het karakterblad van Lev mee als stijlreferentie, maar teken een andere persoon. Bestand: `assets/avatars/a1.webp` t/m `a6.webp`.

| Bestand | Beschrijving |
|---|---|
| `a1` | man, lichte huid, korte bruine haren |
| `a2` | man, donkere huid, kort krullend zwart haar |
| `a3` | man, Oost-Aziatisch, kort zwart haar |
| `a4` | vrouw, lichte huid, bruine staart onder de pet |
| `a5` | vrouw, donkere huid, lang krullend zwart haar of vlechten onder de pet |
| `a6` | vrouw, Oost-Aziatisch, lang zwart haar in een staart onder de pet |

Controle: zelfde stijl, belichting en kadrering in alle zes, gezichten verschillen duidelijk, niemand lijkt op een bestaand persoon. De app toont tot die tijd getekende plaatshouders, en pakt de plaatjes vanzelf op zodra ze er staan.
