# Functies:

> @app.route("/")
def homepage():

Deze functie rendert de homepage.

@app.route("/startquiz", methods=["GET","POST"])
def startquiz():

Deze functie rendert de uitleg pagina van de quiz

>@app.route("/quiz", methods=["GET", "POST"])
Quiz

Deze functie rendert de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. Als laatste roept dit de leaderboard()functie op.

>@app.route("/check", methods=["GET"])
Check()

Deze functie checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returnt het True in met jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.
Anders wordt er alleen aangegeven in welke qua

>@app.route("/leaderboard")
Leaderboard():

Deze functie haalt de top 10 op plus de gegevens van de gebruiker en, rendert de leaderboard.html met deze gegevens.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY1MDY0NTk1MCwxMDYxODQ4MzgyLC0xNz
Q2OTA3NjY4LC0xODc3NDk3MDUxLDg3ODMxNzg4MSwtMTQ3Mjgz
Mzc5NywtMTUzMjQyMDA2OSwtMTk1NTMxMDUxNV19
-->