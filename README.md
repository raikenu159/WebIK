# Kwik Kwiz
### Projectleden 
* Daan van Baarsen, 
* Una Garcia, 
* Sem Kjaer, 
* Soufiane Zouli

## Samenvatting
Op onze webapplicatie is het mogelijk zijn om  multiple choice trivia quizzes af te nemen onder een tijdslimiet. De quizzes worden individueel afgenomen, dus er is geen directe multiplayer. Wel is er een leaderboards-pagina , waar de tien hoogste scores getoond worden. Zo is er toch nog een vorm van concurrentie tussen verschillende spelers. Na een quiz afgenomen te hebben kan de gebruiker grafieken zien die de behaalde score per onderdeel en soort vraag tonen. Ook kan de gebruiker een tabel zien met daarin alle beantwoorde vragen met het gegeven antwoord en het correcte antwoord.

## Video
![https://www.youtube.com/watch?v=GnmT6GnKVR8](Video)

## Afbeeldingen
**Homepagina met uitleg quiz**
![Homepagina](https://i.imgur.com/I1EepTC.png)
**Quizvraag pagina type 1 meerkeuze**
![Quizvraag pagina meerkeuze](https://i.imgur.com/gobQsLO.png)
**Quizvraag pagina type 2 boolean**
![Quizvraag pagina boolean](https://i.imgur.com/ATSs2sh.png)
**Quizvraag pagina tijd verlopen zonder top 10 score behaald te hebben**
![Quizvraag pagina tijd verlopen zonder top 10 score behaald te hebben](https://i.imgur.com/2KWoOco.png)
**Quizvraag pagina tijd verlopen top 10 score behaald**
![Quizvraag pagina tijd verlopen top 10 score behaald](https://i.imgur.com/oSkyIT5.png)
**Leaderboards pagina**
![Leaderboards pagina](https://i.imgur.com/1Ksmhjj.png)
**Barcharts pagina**
![Barcharts pagina](https://i.imgur.com/IIAyq8s.png)![Barcharts pagina](https://i.imgur.com/5zJP0vX.png)
**Question results pagina**
![Question results pagina](https://i.imgur.com/V60LQRy.png)
## Features
1. De vragen in de quizzes komen uit Online Trivia Database (https://opentdb.com)
2. Alle gebruikers nemen een quiz af die vragen bevat uit een aantal verschillende categorieën die 45 of meer vragen bevatten in Open Trivia Database.
3. De quizzes zijn multiple choice.
4. Gebruikers kunnen ervoor kiezen om een vraag over te slaan zonder tijd te verliezen.
5. Elke quiz begint met een tijdslimiet van een minuut.
6. Gebruikers verdienen extra tijd met elke goed beantwoorde vraag.
7. Gebruikers behalen punten met elke goed beantwoorde vraag.
8. Gebruikers behalen meer punten bij het goed beantwoorden van moeilijkere vragen.
9. Er is een leaderboards-pagina met daarin de 10 gebruikers met de hoogste scores, hun scores en de datum waarop de score is behaald.
11. Alleen als een gebruiker een score heeft behaald die in de top 10 zit, wordt er om een username gevraagd.
en gebruiker vanuit de quiz naar de leaderboards-pagina gaat, kan de net behaalde score verwijderd worden. 
13. In de chart-page kan de gebruiker zien hoeveel punten die behaalde per categorie.
1. In de question_result-page kan de gebruiker alle vragen zien die die heeft beantwoord, met het gegeven antwoord en het correcte antwoord.

## Repository gids

Onze repository heeft de naam 'WebIKTrivia02'. Bij het bezoeken van de repository staan er 6 items in de lijst. Drie van deze items zijn mappen, waar we zo op in gaan, de andere drie items zijn bestanden:

 - application.py
 - README.md
 - trivia.db
 
 **Het eerste** bestand 'Application.py' bevat de volledige backend code in python. Uitleg van de functies zit in het commentaar binnen het bestand.
 
**Het tweede** bestand 'README.md' is het huidige bestand dat u nu leest.

**Het derde** en laatste bestand 'trivia.db' is de database waarop ons project werkt. Hierin wordt de user id (en hiermee de session id), de username (mocht speler in de top 10 zitten) de behaalde score en de datum waarop de score is behaald, bijgehouden.

Vervolgens de **3 mappen** in de repository:

 - doc
 - static
 - templates

In de **doc-map** vind je één map:

- /afbeeldingen: hierin staan alle afbeeldingen die gebruikt worden in de README file.

In de **static-map** vind je:

- /js: Hierin staan alle gebruikte javascript files opgeslagen.

- styles.css: het bestand voor de styling van de webpagina's.

- Verder staan hier alle afbeeldingen die gebruikt worden op de webpagina's.

In de **templates-map** vind je:

* Alle HTML-files waaruit de trivia web-applicatie bestaat.

## Werkverdeling

Over het algemeen is het werk vrij goed verdeeld over de groepsleden. Iedereen heeft aan elk onderdeel van het project een bijdrage geleverd en ook aan elk aspect van de applicatie gewerkt. Toch was er tussen de groepsleden enige vorm van specialisatie. 
 
**Daan van Baarsen**
 - Backend/database communicatie
 - Layout homepage
 - Leaderboard

**Sem Kjaer**
- Functies in de backend
- Werken met de API
- Backend/database communicatie

**Una Garcia**
- Quizpagina passend maken op verschillende apparaten
- HTML & CSS
- Projectvoorstel (README) 

**Soufiane Zouli**
- Javascript (frontend)
- HTML & CSS (layout)
- Textfiles bijgehouden (README)
elke mapjes er zijn.*


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE5MjU5MzUwLDE1NTYxOTgzMjksNDc4Nz
E0NTQ4XX0=
-->