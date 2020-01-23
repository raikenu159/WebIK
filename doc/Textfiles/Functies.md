# Functies:

> @app.route("/")
def homepage():

Deze functie rendert de homepage.

>@app.route("/startquiz", methods=["GET","POST"])
def startquiz():

Deze functie rendert de uitleg pagina van de quiz

>@app.route("/quiz", methods=["GET", "POST"])
def quiz()

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

Deze functie verwijderd de user zijn/haar positie in de leaderboard, mocht hij/zij het nog een keer willen proberen onder dezelfde username.

>@app.route("/barchart")
def barchart():

Deze functie rendert de html pagina 'barchart' waarin specifieke data staat van de zojuits gemaakte quiz. Denk hierbij aan score per category en per moeilijkheidsgraad.

>@app.route("/load_questions", methods=["GET"])
def load_questions():

Deze functie vraagt vanuit de API een array van vragen aan per categorie, en zet deze vragen in gerandomiseerde volgordes in de 'questions' lijst. vervolgens worden de juiste en onjuiste antwoorden uit elkaar gehouden, en worden alle vragen met antwoorden in de sessie meegegeven naar de frontend d.m.v. jsonify.

>@app.route("/check_answer")
def check_answer():

Deze functie 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1MDcyOTE3OSwxMDYxODQ4MzgyLC0xNz
Q2OTA3NjY4LC0xODc3NDk3MDUxLDg3ODMxNzg4MSwtMTQ3Mjgz
Mzc5NywtMTUzMjQyMDA2OSwtMTk1NTMxMDUxNV19
-->