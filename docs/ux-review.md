# UX-review Lever-up (2026-10-11)

Twee beoordelingen: `ux-judge` (26 wetten, op code) en `impeccable` design review (live app, 390 px). Detectorscan: 0 bevindingen (ziet alleen statische code). Design-score 26/40.

## Top 8, op winst (ux-judge)

1. **Oefening uitgelicht:** Start timer staat onder de vouw, ver van de klok. Zet hem direct onder de klok (of sticky), hero naar 16/10. Na een voltooide tijdset de volgende set aanvinken en de rust starten.
2. **Streak:** "dagen op rij" breekt elke rustdag (je traint 3x per week) en wegen houdt hem kunstmatig in leven. Voorstel: weken op rij met 3 sessies. Wijkt af van de brief ("dagen op rij"), dus beslissing voor Jordy.
3. **Afronden -> bonuskaart:** nu een toast van 2,2 s. Maak een afsluitpaneel bovenaan Kaarten ("Sessie A klaar, 9 sets, week 2/3, trek je bonuskaart"), undo-toast, confetti alleen bij een rangstijging.
4. **Carrousel:** selectie en trekking lopen niet gelijk (scrollen selecteert alleen na een trekking). Maak scrollen altijd selecteren.
5. **Train:** toon "5 van 9 sets" bovenaan (`remainingSets` bestaat al, wordt niet gebruikt).
6. **Toegankelijkheid:** timerknop heeft label "Rusttimer sluiten" (aftellen wordt niet voorgelezen); tabbalk als `<nav>`; focus herstellen na `render()`; carrousel `role=region`; Level up als `role=dialog` met focus en Escape; geluid en Wake Lock voor timers (iOS trilt niet).
7. **Voortgang:** typefout "Weekelijkse" -> "Wekelijkse"; doelen direct onder de ring; badge-criteria zichtbaar ("2/5 sessies"); badge "Consistentie-koning" permanent bewaren; weekletters Zo Ma Di Wo Do Vr Za; ringlabel "Weekdoelen".
8. **Foutpaden:** native `confirm` vervangen; plan-opslaan met preview en waarschuwing bij lopende sessie; Gewicht als formulier met inline fout; Nederlandse datums; History API zodat terug niet de app verlaat.

## Overig

- Terugknop leest als titel ("Sessie A"): zet "Terug" erbij.
- Train en Kaarten missen een schermtitel.
- Voortgang-icoon is een klok; neem een ring- of staafje-icoon.
- Rusttimer-pill dekt de onderste chiprij en blijft op elk tabblad staan.
- Kleine teksten (11-12 px) en grijze vraagtekens halen het contrast niet.
- Hero-crossfade loopt oneindig (WCAG 2.2.2).
- "Andere" kan oneindig herrollen.
- Sessie met 1 set telt al als sessie, zonder bevestiging of ongedaan maken.

## Design review (impeccable): Lev vs UI

- Lev is warm, vlak, met dikke contouren; de UI is koud, dun, tint-op-tint, één mintgroen dat overal staat.
- Eén font zonder eigen stem voor titels en getallen.
- Train: vier grote lege gestippelde vlakken lezen als gat, niet als plaatshouder.
- Eind van een sessie is een toast, geen moment.
- Richting "vlak en stevig": 2 px donkere rand, harde schaduw zonder blur, duidelijk lichtere kaarten, groen alleen voor "nu doen" en "gedaan", eigen display-font, de pet-"O" als vormmotief, compacte plaatshouders, eigen afrondscherm met Lev.
- Open beslissingen voor Jordy: accent mint of lime (brief: smaragd/teal, lime alleen pet); warme huidtint alleen voor illustratievlakken; copy in Lev's stem.

# Ronde 2 (2026-10-11): sessiebouwer, rangen, Lev-quotes

Op code, door `ux-judge`. Uitkomst: voorwaardelijk goedgekeurd, een injunctie.

## Direct opgelost
- **Per kant / per been ging verloren** in de bouwer (`entryFrom`): "10 per kant" werd "10". Nu een `per`-veld, zichtbaar in bouwer, Train en uitgelicht scherm.
- **Eén rangnaam overal:** header, rangpaneel, "nog x tot ..." en ladder tonen nu de volledige titel (was korte naam in de ene en lange in de andere). Lange titels breken af.
- **Geen dubbele quote bij rangstijging:** het afrondpaneel toont dan alleen de feiten, Level up geeft de quote.
- **Reps-veld** opent het tekstklavier, zodat "20s" op een telefoon te typen is.

## Open, op winst gerangschikt
1. **Bouwer: ongedaan maken en bevestigen.** Programma laden overschrijft A en B, verwijderen en Terug gooien werk weg. Voorstel: "Ongedaan" 5 seconden, controle bij Terug en tabwissel. Middel.
2. **Voortgang herordenen** (zes blokken, ~2000 px; "nog x" en "3 sessies" staan op meerdere plekken): rang, weekring met doelen en reeks erin, badges; de ladder en opbouw per spiergroep inklapbaar. Middel.
3. **Bouwer: sticky Opslaan en compactere oefeningrij.** Een rij is waarschijnlijk drie regels (344 px in een vak van ~326). Opslaan staat 1700 px lager. Middel.
4. **Bibliotheek:** markeer oefeningen die al in de sessie staan, tel ze, geef eigen oefening focus terug. Klein.
5. **Focus herstellen** op het reps-veld en na laden van een programma; programmaknop niet "ingedrukt" laten na handmatige wijziging. Klein.
6. **Kleine dingen:** één term (Sessie bouwen of samenstellen), geen herhaalde rangquote bij elk bezoek aan Voortgang, validatiefout inline met `aria-live`, dezelfde SESSION_LINE niet twee keer achter elkaar. Klein.
