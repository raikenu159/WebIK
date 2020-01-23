# Functies:

> @app.route("/")
def homepage():

Deze functie rendert de homepage.

>@app.route("/startquiz", methods=["GET","POST"])
def startquiz():

Deze functie rendert de uitleg pagina van de quiz

>@app.route("/quiz", methods=["GET", "POST"])
Quiz

Deze functie rendert de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. Als laatste roept dit de leaderboard()functie op.

>@app.route("/check", methods=["GET"])
def check()

Deze functie checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returnt het True in jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.
Anders wordt er alleen aangegeven in welk kwartier de score van de user valt en wordt een jsonified False gereturnd. 

>@app.route("/leaderboard")
def leaderboard():

Deze functie haalt de top 10 op plus de specifieke scores per categorie van de huidige user. Vervolgens wordt de leaderboard.html pagina gerendert  met deze gegevens.

>@app.route("/delete_username")
def delete_username(): 

Deze 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMjA0Mjc3OTAsMTA2MTg0ODM4MiwtMT
c0NjkwNzY2OCwtMTg3NzQ5NzA1MSw4NzgzMTc4ODEsLTE0NzI4
MzM3OTcsLTE1MzI0MjAwNjksLTE5NTUzMTA1MTVdfQ==
-->