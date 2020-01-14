Functies:

@app.route("/")
Homepage():
Deze functie rendered de homepage

@app.route("/quiz", methods=["GET", "POST"])
Quizethod:
Deze functie rendered de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. Als laatste roept dit de leaderboard() functie op.

@app.route("/check", methods=["GET"])
C functie checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returned het True in met jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.

@app.route("/leaderboard")
Leaderboard():
Deze functie haalt de top 10 op plus de gegevens van de gebruiker en, rendered de leaderboard.html met deze gegevens.
<!--stackedit_data:
eyJoaXN0b3J5IjpbODc4MzE3ODgxLC04MjU2MDAxNjAsLTE0Nz
I4MzM3OTcsLTE1MzI0MjAwNjksLTE5NTUzMTA1MTVdfQ==
-->