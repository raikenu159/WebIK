# Projectvoorstel IK02 Trivia spel
### Projectleden 
* Daan van Baarsen, 
* Una Garcia, 
* Sem Kjaer, 
* Soufiane Zouli

## Samenvatting
Op onze webapplicatie is het mogelijk zijn om  multiple choice trivia quizzes af te nemen onder een tijdslimiet. De quizzes worden individueel afgenomen, dus er is geen directe multiplayer. Wel is er een leaderboards-pagina , waar de tien hoogste scores getoond worden. Zo is er toch nog een vorm van concurrentie tussen verschillende spelers. Na een quiz afgenomen te hebben kan de gebruiker grafieken zien die de behaalde score per onderdeel en soort vraag tonen. Ook kan de gebruiker een tabel zien met daarin alle beantwoorde vragen met het gegeven antwoord en het correcte antwoord.

## Schetsen
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
![Leaderboards pagina](https://i.imgur.com/cyqAbDQ.png)
**Barcharts pagina**
![Barcharts pagina](https://i.imgur.com/IIAyq8s.png)![Barcharts pagina](https://i.imgur.com/5zJP0vX.png)
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
10. Alleen als een gebruiker een score heeft behaald die in de top 10 zit, wordt er om een username gevraagd.
11. In de chart-page kan de gebruiker zien hoeveel punten die behaalde per categorie.
12. Inde question_result-page kan de gebruiker alle vragen zien die die heeft beantwoord, met het gegeven antwoord en het correcte antwoord.


## Minimum viable product
Voor een minimum viable product willen we in ieder geval de features 1 t/m 10 implementeren.

## Sanity check
De projecteisen zoals ze in de studiewijzer staan voor een trivia site, zijn: 
>"**Trivia.** Gebruikers kunnen triviavragen beantwoorden en op die manier punten scoren. Er is een interessant systeem om van andere gebruikers te winnen. De vragen komen uit een online triviadatabase zoals http://jservice.io” (WebIK Syllabus, 2020). 

Uitgaande hiervan zijn onze gekozen features voor een minimum viable product voldoende voor de projecteisen.

## Controllers
De controller is application.py. In dit bestand worden de volgende functies uitgevoerd:
###  Routes
#### @app.route("/")
Deze route roept de homepage (index.html) aan.
```py
@app.route("/")
def homepage():
    """Homepage"""
    # deze functie laadt alleen de homepage
    return render_template("index.html")
```
#### @app.route("/quiz", methods=["GET", "POST"])
Deze route rendert de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. Als laatste roept dit de leaderboard() functie op.
```py
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Take quiz"""

    if request.method == "POST":
        # nadat de check functie is uitgevoerd worden de username(als de gebruiker in de top 10 zit) en de score gesubmit
        # deze functie voegt deze dan toe aan de database zodat deze op de leaderboard weergegeven kunnen worden
        id = session["user_id"]
        username = request.form.get('username')
        scoreTotaal = request.form.get('scoreTotaal')
        # ook voegen de de score per catagorie toe om de gebruiker inzicht te gevenen in zijn prestaties per catagorie
        score1 = request.form.get('score1')
        score2 = request.form.get('score2')
        # etc. (catagorieen nog te bepalen)
        db.execute("INSERT INTO scores (id, username, scoreTotaal, score1, score2, etc., date) VALUES (:sessionid, :username, :score)",
            id = id,
            username = username,
            scoreTotaal = scoreTotaal,
            score1 = score1,
            score2 = score2,
            etc)

        return render_template("leaderboard.html")
	else:
	        # voordat de quiz begint word er een row binnen de database met daarin een user id aangemaakt voor de gebruiker
	        # daarna word een request gestuurd naar de api voor de vragen die in de quiz moeten komen (50 per categorie, 5 categorieen)
	        # dan worden de vragen om en om gesorteerd zodat de gebruiker ongeveer hetzelfde aantal vragen uit elke categorie krijgt
	        return render_template("quiz.html")
```
#### @app.route("/check", methods=["GET"])
Deze route checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returnt het True in met jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.
```py
@app.route("/check", methods=["GET"])
def check():
    """Return true if achieved score is in top 10"""
    # voordat de quiz.html de score submit checken we of de gebruiker in de top 10 van gebruikers zit
    # we returnen dan True/False naar de quiz.html, deze zal de gebruiker om een naam vragen als hij
    # in de top 10 zit zodat we die kunnen laten zien op de leaderboard en anders een pop up geven dat de quiz voorbij is
    top10 = db.execute("SELECT TOP 10 * FROM scores ORDERED BY score")

    username = request.args.get("username")

    # Set result to false if username is one character or less
    if len(username) <= 1:
        return jsonify(False)

    # Check if username is in use
    usernameFound = db.execute("SELECT * FROM users WHERE username = :username",
                        username = username)
    if usernameFound:
        return jsonify(False)

    return jsonify(True)
```

#### @app.route("/leaderboard")
Deze route haalt de top 10 op plus de gegevens van de gebruiker en, rendert de leaderboard.html met deze gegevens.
```py
@app.route("/leaderboard")
def leaderboard():
    """Display the current leaderboard and some statistics about the users performance"""
    # hier halen we de data op uit de database, die we nodig hebben om de leaderboard en de statistieken te laten zien
    top10 = db.execute("SELECT TOP 10 username, scoreTotaal FROM scores ORDERED BY score")
    userdata = db.execute('SELECT * FROM scores WHERE id = :id')
    # deze geven we mee wanneer we de leaderboard pagina renderen
    return render_template('leaderboard.html', top10, userdata)
```

## Frameworks & Plugins

### Bootstrap
 - Bootstrap is een gratis open source CSS framework oorspronkelijk ontwikkeld voor intern gebruik door de ontwikkelaars van Twitter. Het framework heeft standaard al een boel standaard functies waardoor het ontwikkelen van een responsive website zeer snel gaat.
 - In layout.html (uit Finance)
 - http://getbootstrap.com/docs/4.1/
 - https://bootswatch.com/
 - https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css
 
### Flask

[Flask](https://flask.palletsprojects.com/) is een webraamwerk dat tools, bibliotheken en technologieën biedt die geschikt zijn om een webapplicatie te bouwen. Deze webapplicatie kan komen in de vorm van webpagina's, blogs, of zelfs een uitgebreide webgebaseerde agenda-app of een commerciële site.
Flask is een van de beste [micro-frameworks](https://en.wikipedia.org/wiki/Microframework), omdat het weinig tot geen afhankelijkheden heeft van externe bibliotheken.

- Uit application.py (in Finance)
```python
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjMwNTY0MTQyLDE3NTAyODUzMywtMzU0Nz
A4MzcwLC0xMjgxMjE3MDMsLTEyNTY3NjAxOCwtNjEwMjAyNjU4
LC0xMjU1MjY5OTA3LDEyODYwNDc4MDYsLTE3Mjg0MDY2ODcsLT
EwMTQ1NDkwNywtMTk2NDQ2NzYwMiwtNjEzMTkyMDE4LDQwNDk2
ODE2MF19
-->