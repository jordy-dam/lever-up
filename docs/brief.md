# Lever-up: opdracht voor Claude Code

Persoonlijke calisthenics-app (parallettes en ringen) voor één gebruiker, in het Nederlands. Een werkende versie bestaat al als één HTML-bestand (`lever-up.html`). Die heeft de logica maar een tijdelijke look met getekende SVG-poppetjes. Doel van deze opdracht: de app omzetten naar de stijl van "De Nieuwe Lev" (donker, ingetogen, realistisch karakter) en de opbouw uitbreiden naar de schermen hieronder, met echte plaatjes in plaats van SVG-poppetjes.

## Werkwijze

1. Open `lever-up.html` in de browser en gebruik hem, zodat je weet wat er al werkt.
2. Houd de logica en het datamodel intact. Verander eerst alleen de presentatie, daarna pas de nieuwe schermen.
3. Gebruik de skill `impeccable` (of een vergelijkbare design-skill) voor de UI. Houd de stijl rustig: geen regenboogkleuren en geen felle gloed.
4. Bouw per scherm en test na elk scherm in de browser (mobiel formaat, ongeveer 390 px breed).
5. Eerst alle schermen met tijdelijke plaatjes (plaatshouders), pas daarna de echte plaatjes erin.

Aanname: een statische webapp (HTML, CSS en JS, eventueel Vite) zonder backend, met opslag in `localStorage`. Kies zelf de eenvoudigste opzet die als PWA op de telefoon kan.

## Datamodel (behouden, nu in `localStorage` onder `ringwerk-v1`)

```json
{
  "plan": { "A": [{"n":"Parallette push-ups","sets":3,"reps":"8"}], "B": [] },
  "sessions": [{"date":"2026-10-11","type":"A","sets":9}],
  "weights": [{"date":"2026-10-11","kg":80.4}],
  "cards": {"p1a": 2},
  "cardLog": ["2026-10-11"],
  "draft": {"type":"A","done":{"0":[true,false,false]}},
  "updatedAt": 0
}
```

- `reps` is een tekst: `"8"` is herhalingen, `"20s"` is een tijd in seconden. Gebruik dat voor de timer-modus (scherm 1).
- Sessie A en B wisselen af, 3 sessies per week.
- Gewicht: dagelijks wegen, getoond als weekgemiddelde (week begint op maandag). Het verschil met vorige week mag getoond worden, maar de app maakt daar geen oordeel over.
- Rusttimer van 90 seconden na elke set.
- Rangen (hernoemd 2026-10-11, zie docs/lev-teksten.md; oorspronkelijk Kersverse hanger, Ringkind, Ringklimmer, Ringbaas, Ringleader): 0 sessies "Groentje" (Zwaartekracht Groentje), 3 "Veertje" (Stalen Veertje), 9 "Bar Baas", 18 "Lucht Ninja", 36 "Legende" (Anti-Zwaartekracht Legende). **Gewijzigd 2026-10-11:** een rang vraagt sessies én beheerste oefeningen: Veertje 3 en 2, Bar Baas 9 en 6, Lucht Ninja 18 en 12, Legende 36 en 18 (van de 24 oefeningen). Bij een nieuwe rang verschijnt een "Level up!"-scherm.
- Weekdoelen: 3 sessies, 1 bonuskaart, 4 weigh-ins. Het percentage in de ring is het gemiddelde van die drie.
- Badges nu: Eerste sessie, Vijf keer raak (5 sessies), Consistentie-koning (3 sessies in een week), Kaartenjager (6 unieke kaarten). Uitbreiden mag.

## Kaartendeck (24 kaarten, ID blijft behouden)

Vier soorten: duwen (`p`), trekken (`t`), core (`c`), benen (`l`). Drie niveaus. Per soort en niveau twee kaarten. Na een sessie mag je een bonuskaart trekken op een gekozen niveau en markeer je hem als "gedaan". De verzameling telt per kaart hoe vaak je hem deed.

| id | oefening | hoeveelheid |
|---|---|---|
| p1a, p1b | Incline push-ups, Langzame wall push-ups | 10 reps |
| p2a, p2b | Push-ups, Pike push-ups | 8 en 6 reps |
| p3a, p3b | Parallette push-ups, Ring push-ups | 8 en 6 reps |
| t1a, t1b | Ring rows hoge hoek, Scapula-hang | 8 reps |
| t2a, t2b | Ring rows lage hoek, Chin-up negatives | 10 reps, 3 x 5 sec |
| t3a, t3b | Pull-ups, Ring rows voeten verhoogd | 5 en 8 reps |
| c1a, c1b | Dead bug, Plank | 10 per kant, 30 sec |
| c2a, c2b | Hollow hold, Hanging knee raises | 20 sec, 8 reps |
| c3a, c3b | Tuck L-sit op parallettes, Hollow rocks | 15 sec, 15 reps |
| l1a, l1b | Squats, Glute bridges | 15 reps |
| l2a, l2b | Split squats, Wall sit | 8 per been, 40 sec |
| l3a, l3b | Pistol squat naar bank, Jump squats | 5 per been, 10 reps |

## Schermen (nieuwe opbouw)

1. **Oefening uitgelicht**: groot plaatje van de oefening bovenaan, titel, een timer ("00:08 / 00:10") voor tijdsoefeningen, daaronder sets, reps en tijd (bijvoorbeeld 3 x 10 sec), en naast de gegevens een spierkaart met de betrokken spiergroepen gemarkeerd. Knop "Start timer". Bereikbaar door een oefening in het trainingsoverzicht aan te tikken.
2. **Kaartendeck**: schakelaar voor Niveau 1/2/3, een carrousel van kaarten waarvan de middelste licht oplicht (groene rand), een label per kaart, en de knop "Trek een kaart". Onder het deck blijft de verzameling van 24 kaarten staan (niet-gevonden kaarten als silhouet).
3. **Trainingsoverzicht** (vervangt de huidige Train-lijst): per oefening twee plaatjes naast elkaar, de start- en de eindpositie, met de naam eronder en de set-knoppen. Onderaan "Start training". Sessie A/B-schakelaar blijft bovenaan, plus "Plan aanpassen".
4. **Progressie en badges**: grote ring met het weekpercentage en het woord "Voltooid", twee tot vier badges als troffee of medaille, en weekdoelen met aantallen (sessies, bonuskaart, weigh-ins, totale trainingstijd).
5. **Rang en reeks**: avatar van Lev met de huidige rang, het aantal dagen op rij en vlam-streak. Een vriendenranglijst uit het voorbeeld is een latere versie: dat vraagt gedeelde opslag tussen mensen en hoort niet bij deze opdracht.

De tabbalk onderaan wordt: Train, Kaarten, Voortgang, Gewicht. (Gewijzigd 2026-10-11: de vierde tab is Profiel, met Gewicht daarin.)

## Spiergroepen

Gebruik deze 16 regio's als vaste ID's (de spierkaart en de data delen ze): `chest, front_delt, rear_delt, triceps, biceps, forearms, lats, upper_back, lower_back, abs, obliques, hip_flexors, glutes, quads, hamstrings, calves`.

Primair is fel gemarkeerd en secundair is zachter gemarkeerd. De indeling is indicatief (algemene bewegingsleer, geen medisch advies).

| oefening | primair | secundair |
|---|---|---|
| Parallette push-ups | chest, front_delt, triceps | abs |
| Incline push-ups | chest, triceps | front_delt, abs |
| Langzame wall push-ups | chest, triceps | front_delt |
| Push-ups | chest, triceps, front_delt | abs |
| Pike push-ups | front_delt, triceps | upper_back, chest |
| Ring push-ups | chest, front_delt, triceps | abs, obliques |
| Ring rows (hoge en lage hoek) | lats, upper_back, biceps | rear_delt, forearms, abs |
| Ring rows voeten verhoogd | lats, upper_back, rear_delt | biceps, forearms, abs |
| Scapula-hang | upper_back, lats | forearms |
| Chin-up negatives | biceps, lats | forearms, upper_back |
| Pull-ups | lats, biceps, upper_back | forearms, abs, rear_delt |
| Front lever hold (nieuw, uit het voorbeeld) | lats, abs, rear_delt | biceps, forearms, glutes, upper_back |
| Dead bug | abs, hip_flexors | obliques |
| Plank | abs, obliques | front_delt, glutes |
| Hollow hold | abs, hip_flexors | quads |
| Hollow rocks | abs, hip_flexors | quads |
| Hanging knee raises | hip_flexors, abs | forearms, obliques |
| Tuck L-sit op parallettes | hip_flexors, abs, triceps | quads, front_delt, forearms |
| Squats | quads, glutes | hamstrings, lower_back, calves |
| Glute bridges | glutes, hamstrings | lower_back |
| Split squats | quads, glutes | hamstrings, calves |
| Wall sit | quads | glutes, calves |
| Pistol squat naar bank | quads, glutes | hamstrings, calves, abs |
| Jump squats | quads, glutes, calves | hamstrings |

**De spierkaart bouw je zelf als SVG, niet als gegenereerd plaatje.** Teken een eenvoudig lichaamssilhouet van voren en van achteren, met per regio een eigen `path` met het ID hierboven, zodat je regio's per oefening aan en uit kunt zetten. Een bestaand SVG met vrije licentie mag ook, als de licentie is nagekeken. Een AI-plaatje is hiervoor niet geschikt, want de regio's zijn dan niet los te schakelen.

## Beelden (te genereren met een beeldgenerator, niet in code)

**Het karakter, "Lev":** een atletische man van rond de dertig met een korte donkere haardracht, een donkerblauwe pet met een lime-groen ringetje als logo, een blauw sportshirt, een donkere short en sportschoenen. Een vriendelijke, zelfverzekerde uitdrukking, een licht verhaalde of lichtelijk 3D-achtige illustratiestijl, goed van opzet. Geen echt persoon nabootsen en geen bestaande karakters of kaartenreeksen kopiëren.

Werk in deze volgorde, zodat Lev er overal hetzelfde uitziet:

1. **Karakterblad** (1 plaatje): Lev van voren, opzij en van achteren, plus 6 gezichtsuitdrukkingen (blij, geconcentreerd, juichend, moe, verbaasd, trots). Gebruik dit blad als referentie bij alle volgende plaatjes.
2. **Posesset** (8 plaatjes, transparante achtergrond): hangend aan de ringen, front lever, push-up op parallettes, hollow hold, squat, juichend, moe, duim omhoog.
3. **Oefeningplaatjes in twee standen** (start en eind, dezelfde camerahoek en kadrering, 4:3), voor deze acht oefeningen: Parallette push-ups, Ring rows, Pike push-ups, Hollow hold, Split squats, Tuck L-sit, Dead bug, Ring rows voeten verhoogd. Dat zijn 16 plaatjes, plus 2 voor Front lever hold.
4. **Kaartplaatjes** (24, staand formaat): eerst 4 per soort (duwen, trekken, core, benen) en later een eigen plaatje per kaart. Hergebruik waar het kan de oefeningplaatjes.
5. **Badges en rangen** (ongeveer 10): troffee of medaille per badge (Push-up held, Consistentie-koning en de overige), plus 5 rangemblemen.
6. **App-icoon** (1 plaatje, 1024 x 1024 px).

Specificaties: PNG of WebP met transparante achtergrond, minstens 1024 px op de lange zijde, lichtinval altijd van linksboven, ruime marge rond het onderwerp zodat de app kan bijsnijden. Bestandsnamen: `assets/lev/pose-hang.png`, `assets/exercises/parallette-pushups-start.png` en `-end.png`, `assets/cards/p3a.png` (het kaart-ID), `assets/badges/push-up-held.png`, `assets/ranks/ringleader.png`. Genereer eerst de plaatjes die schermen 1 en 3 nodig hebben, want die tonen het meest.

## Stijl ("De Nieuwe Lev")

- Donker marineblauw (ongeveer `#0e1830` als achtergrond), kaarten een tint lichter, en één ingetogen groene accentkleur (smaragd of teal) voor actieve knoppen, geselecteerde niveaus en de rand van de middelste kaart. De pet gebruikt dezelfde lime-kleur als logo.
- Rustige typografie, afgeronde hoeken, weinig verlopen. Geen regenboogtitel, geen sterretjes, geen zware gloed.
- Het plaatje van Lev en de oefeningen mag de ruimte vullen. De rest van de interface blijft stil.
- Houd rekening met reduced motion, leesbare contrasten en een grote aanraakdoelen (minstens 48 px).

## Niet doen

- De komische tekstballonnen van het vorige karakter kun je behouden of vervangen. Overleg dat met de gebruiker, want de toon verschuift van grappig naar serieus.
- Geen backend, geen accounts en geen advertenties.
- Verzin geen oefeningen in het plan: de plaatshouders in `plan.A` en `plan.B` zijn nog niet het echte programma. Vraag de gebruiker om zijn echte oefeningen.
