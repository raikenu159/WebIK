Functies:
Homepage():
Deze functie rendered de homepage

Quiz():
Methoden: get en post
Deze functie rendered de quiz, hierna zal de rest van de quiz via javascript uitgevoerd worden. Nadat de quiz af is zal deze functie de database updaten met de behaalde score (totaal en per categorie), en mits de gebruiker in de top 10 beland ook met een username. 

Check():
Methoden: get
Deze functie checkt of de score van de gebruiker genoeg is om in de top 10 te komen, zo ja returned het True in met jsonify, in dat geval zal de gebruiker via javascript gevraagd worden een username op te geven.

Leaderboard():
Deze functie haalt de top 10 op plus de gegevens van de gebruiker en rendered leaderboard.html met deze gegevens.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwODUzODU3OTMsLTE1MzI0MjAwNjksLT
E5NTUzMTA1MTVdfQ==
-->