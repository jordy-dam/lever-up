# Lever-up

Persoonlijke calisthenics-app (parallettes en ringen), één gebruiker, Nederlands. Statische webapp, geen backend, opslag in `localStorage` (`ringwerk-v1`), doel: PWA op de telefoon.

## Lees eerst

- `docs/brief.md`: de volledige opdracht (werkwijze, datamodel, kaartendeck, schermen, spiergroepen, beelden, stijl). Dit is de bron van waarheid.
- `docs/reference/de-nieuwe-lev-mockup.png`: stijlreferentie "De Nieuwe Lev". Alleen als sfeer en indeling, niet pixel voor pixel.
- `docs/reference/schermen-mockup.webp`: de vijf schermen naast elkaar (opbouw, spierkaart, kaartendeck, badges). Het vijfde scherm (Community en ranglijst) is een latere versie, niet bouwen.
- `reference/lever-up-original.html`: onaangeroerde originele versie. Nooit aanpassen.
- `lever-up.html`: werkkopie waar we in bouwen.

## Werkwijze (uit de brief)

1. Open de app in de browser en gebruik hem eerst.
2. Logica en datamodel blijven intact. Eerst alleen presentatie, daarna nieuwe schermen.
3. Eén scherm tegelijk. Laat het zien (mobiel, 390 px breed) en wacht op akkoord voor het volgende.
4. Eerst alle schermen met plaatshouders, pas daarna echte plaatjes.
5. UI via de `impeccable`-skill. Stijl rustig: donker marineblauw (`#0e1830`), één accentkleur (lime), geen regenboog, geen felle gloed.

## Harde regels

- Geen backend, accounts of advertenties.
- Verzin geen oefeningen in `plan.A` / `plan.B`: vraag Jordy om het echte programma. De voorgestelde programma's in de sessiebouwer komen alleen uit de 24 kaarten van de brief.
- Kaart-ID's (`p1a` ... `l3b`) en de 16 spiergroep-ID's blijven vast.
- Spierkaart: AI-plaatje voor- en achterkant (`assets/muscles/front.png`, `back.png`) plus per regio een masker (`assets/muscles/m/<view>-<regio>.png`, gemaakt door segmentatie van de vlakken). Regio-ID's blijven de 16 vaste ID's.
- Aanraakdoelen minstens 48 px, reduced motion respecteren.
- Tekstballonnen van het oude karakter: eerst met Jordy overleggen (toon verschuift van grappig naar serieus).

## Team (zie ook globale AGENTS.md)

Geen vijfde rol. Voor dit project:

- Bouwen en design in code: hoofdsessie met `impeccable`.
- UX-check per afgerond scherm: Operator, `ux-judge`.
- Prompts voor de beeldgenerator (karakterblad, posesets, kaarten): Storyteller. De plaatjes zelf maakt Jordy in een beeldgenerator, Claude Code kan geen plaatjes genereren.
- Beslissingen met gevolgen: loggen in `DECISIONS.md`.

## Stand van zaken (2026-10-11)

- Klaar: scherm 3 (Train/trainingsoverzicht), scherm 2 (Kaarten), scherm 1 (Oefening uitgelicht), scherm 4 (Voortgang), scherm 5 (Rang en reeks, bovenaan Voortgang) en de gedeelde look (kleuren, knoppen, tabbalk, header). Plaatjes: alleen Parallette push-ups (`assets/exercises/<naam-met-streepjes>-start|end.webp`), de rest is plaatshouder.
- Alle tabs en Level up hebben de nieuwe look en de nieuwe Lev (uitgesneden uit het karakterblad, tijdelijk laag-res). Het oude cartoonkarakter is uit de code gehaald.
- Beelden: promptset voor Gemini staat in `docs/prompts-gemini.md` (stijlblok, vaste ruimte en camera, 8 oefeningen start/eind, 24 kaarten, Lev-poses, badges, rangen, icoon). Jordy maakt ze, Claude zet ze om en plaatst ze.
- Rangen en Lev-teksten staan in `docs/lev-teksten.md` (Groentje, Veertje, Bar Baas, Lucht Ninja, Legende; quotes alleen op Level up, rangpaneel en afrondpaneel, niet tijdens de training). Dit lost de vraag over tekstballonnen grotendeels op: geen ballonnen.
- Geleide sessie (focusscherm, automatische rust met Lev, tijdsoefeningen starten zelf) en eerste-keer-schermen zijn gebouwd. Profiel-tab (naam, Gewicht, instellingen, back-up) is gebouwd; Train is een beknopt overzicht (startkaart plus compacte lijst).
- Gebouwd na de vijf schermen: sessiebouwer (programma's, bibliotheek, aanpassen), rangenladder en opbouw per spiergroep (Voortgang).
- Volgende stap: hosten via https (nodig om op de telefoon te installeren), Lev-stem in copy (open beslissing), echte plaatjes (Lev-posen, kaarten, oefeningen, app-icoon 1024 px). Let op iOS: de geïnstalleerde app heeft een eigen opslag, data uit Safari komt er niet in.
- Lokaal bekijken: `python3 -m http.server 5183` in de repo, dan `http://127.0.0.1:5183/lever-up.html`.
- Eerste-keer-schermen bekijken: voeg `&onboard` toe; korte rust om de geleide sessie te testen: `&rest=3`.
- Voorbeeldgegevens (zonder opslaan): `http://127.0.0.1:5183/lever-up.html?demo`, met Level up-scherm: `?demo=levelup`.
- Look uitproberen: voeg `&tune` toe aan de link (knop "Look" rechtsboven).
