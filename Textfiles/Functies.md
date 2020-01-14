Functies:

@app.route("/")
Homepage():
Deze functie rendered de homepage

@app.route("/quiz", methods=["GET", "POST"])
Quiz():
Deze functie rendered de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. 

Cdef check():
Deze functie checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returned het True in met jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.

Ldef leaderboard():
Deze functie haalt de top 10 op plus de gegevens van de gebruiker en, rendered de leaderboard.html met deze gegevens.
 en g itten th tackdt(httsstkedit.io
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc4OTM0MTg3MiwtMTQ3MjgzMzc5NywtMT
UzMjQyMDA2OSwtMTk1NTMxMDUxNV19
-->