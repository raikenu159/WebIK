# Functies:

> @app.route("/")
Homepage():

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA2MTg0ODM4MiwtMTc0NjkwNzY2OCwtMT
g3NzQ5NzA1MSw4NzgzMTc4ODEsLTE0NzI4MzM3OTcsLTE1MzI0
MjAwNjksLTE5NTUzMTA1MTVdfQ==
-->