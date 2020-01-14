# Projectvoorstel IK02 Trivia spel
### Projectleden 
* Daan van Baarsen, 
* Una Garcia, 
* Sem Kjaer, 
* Soufiane Zouli

## Samenvatting
Op onze webapplicatie zal het mogelijk zijn om gecategoriseerde multiple choice trivia quizzes af te nemen onder een tijdslimiet. De quizzes worden individueel afgenomen, dus er is geen directe multiplayer. Wel zal er een leaderboards-pagina zijn, waar de hoogste scores van gebruikers bijgehouden en getoond zullen worden. Zo is er toch nog een vorm van concurrentie tussen verschillende spelers.

## Schetsen
**Homepagina**
![Homepagina](https://i.imgur.com/m2AtHsf.png)

**Quizvraag pagina**
![Quizvraag pagina](https://i.imgur.com/AWXJi1A.png)

**Leaderboards pagina**
![Leaderboards pagina](https://i.imgur.com/DC73y4T.png)

## Features
1.  Alle gebruikers nemen een quiz af die vragen bevat uit een aantal verschillende categorieën die 45 of meer vragen bevatten in Opentriviadatabase (zie feature 2)
2. De vragen in de quizzes komen uit Open Trivia Database (https://opentdb.com)
3. De quizzes zijn multiple choice.
4. Gebruikers kunnen ervoor kiezen om een vraag over te slaan zonder tijd te verliezen.
5. Elke quiz begint met een tijdslimiet van een minuut.
6. Gebruikers verdienen extra tijd met elke goed beantwoorde vraag.
7. Gebruikers behalen punten met elke goed beantwoorde vraag.
8. Gebruikers behalen meer punten bij het goed beantwoorden van moeilijkere vragen.
9. Er is een leaderboards-pagina met daarin de 10 gebruikers met de hoogste scores, hun scores en de datum waarop de score is behaald getoond worden.
10. Alleen als een gebruiker een score heeft behaald die in de top 10 zit, wordt er om een username gevraagd.


## Minimum viable product
Voor een minimum viable product willen we in ieder geval de features 1 t/m 9 implementeren.

## </p>
<h2 id="sanity-check">Sanity check
</h2>
<p>De projecteisen zoals ze in de studiewijzer staan voor een trivia site, zijn: 
>"**Trivia**“<strong>Trivia</strong>. Gebruikers kunnen triviavragen beantwoorden en op die manier punten scoren. Er is een interessant systeem om van andere gebruikers te winnen. De vragen komen uit een online triviadatabase zoals <a href="http://jservice.io">http://jservice.io</a>” (WebIK Syllabus, 2020). 

Uitgaande hiervan zijn onze gekozen features voor een minimum viable product voldoende voor de projecteisen.

## Controllers
De controller is application.py. In dit bestand worden de volgende functies uitgevoerd:
###  Functies:
@app.route("/")
Homepage():`

Deze functie rendert de homepage

>@app.route("/quiz", methods=["GET", "POST"])
Quiz
Deze functie rendert de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. Als laatste roept dit de leaderboard()functie op.

>@app.route("/check", methods=["GET"])
Check()

Deze 

functie checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returnt het True in met jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.

>@app.route("/leaderboard")
Leaderboard():

Deze functie haalt de top 10 op plus de gegevens van de gebruiker en, rendert de leaderboard.html met deze gegevens.


## Frameworks & Plugins
### Bootstrap
 - Bootstrap is een gratis open source CSS framework oorspronkelijk ontwikkeld voor in</p>
<blockquote>
<p>Writtern gebruik door de ontwikkelaars van Twitter. Het framework heeft standaard al een boel standaard functies waardoor het ontwikkelen van een responsive website zeer snel gaat.
 - In layout.html (uit Finance)
 - http://getbootstrap.com/docs/4.1/
 - https://bootswatch.com/
 - https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css
 
### Flask
[Flask](https://flask.palletsprojects.com/) is een webraamwerk dat tools, bibliotheken en technologieën biedt die geschikt zijn om een webapplicatie te bouwen. Deze webapplicatie kan komen in de vorm van webpagina's, blogs, of zelfs een uitgebreide webgebaseerde agenda-app of een commerciële site.
Flask is een van de beste [micro-frameworks](https://en.wikipedia.org/wiki/Microframework), omdat het weinig tot geen afhankelijkheden heeft van externe bibliotheken.

- Uit application.py (in Finance)
	>from flask import Flask, flash, jsonify, redirect, 
	render_template, request, session
	from flask_session import Session
### Socket.io

Socket.IO is een JavaScript-bibliotheek voor realtime webapplicaties. Het maakt realtime bidirectionele communicatie tussen webclients en servers mogelijk.

- Kan misschien pop-ups genereren, push meldingen versturen naar de gebruikers.
- A.s. vrijdag 17 januari meer over vragen aan begeleiders.

### Datetime.now
- Genereert de datum van het moment van spelen van de trivia game
- Voor de datum in de leaderboards
- In application.py (uit Finance)


with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2MzYxNDA4NiwtNDM5MDQ0MTMwLDQ1MT
Y4MTQ4NSwtNDgxNDgzOTA5LDEwMDQ2MjQyMzksLTI0NjYwODAs
OTI3MjYzNjY5LDU3ODMxNzIzN119
-->